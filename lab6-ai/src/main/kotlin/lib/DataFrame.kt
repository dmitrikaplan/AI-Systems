package lib

import java.io.File
import java.io.FileReader
import java.lang.RuntimeException
import kotlin.system.exitProcess

class DataFrame{

    private var data = HashMap<String, ArrayList<String>>()

    val columns: MutableList<String>

    val size: Int
        get() = first().size

    constructor(columns: MutableList<String>){
        this.columns = columns
    }

    constructor(data: HashMap<String, ArrayList<String>>){
        this.data = data
        this.columns = data.keys.toMutableList()
    }


    fun readFromCSV(path: String) {
        val file = File(path)
        val reader = FileReader(file)

        reader.forEachLine {
            it.split(",").forEachIndexed { index: Int, d: String ->
                if(d.trim() == "") throw RuntimeException()
                if (!data.containsKey(columns[index])) {
                    data[columns[index]] = ArrayList<String>().also { list -> list.add(d) }
                } else {
                    data[columns[index]]!!.add(d)
                }
            }
        }

        reader.close()
    }


    fun drop(column: String): DataFrame {
        val dataCopy = HashMap<String, ArrayList<String>>(data).also {
            it.remove(column)
        }
        return DataFrame(dataCopy)
    }


    fun getColumn(column: String): DataFrame{
        return DataFrame( hashMapOf(column to data[column]!!))
    }

    fun first(): ArrayList<String> =
        data[columns.first()]!!


    operator fun get(column: String): ArrayList<String> {
        return data[column]!!
    }

    operator fun get(columns: List<String>): DataFrame {
        val newData = HashMap<String, ArrayList<String>>()
        columns.forEach {
            newData[it] = data[it]!!
        }
        return DataFrame(newData)
    }

    override fun toString(): String {
        val builder = StringBuilder()
        columns.forEach {
            builder.append("$it:\n")
            builder.append("${data[it]}\n")
        }

        return builder.toString()
    }

    fun mode(column: String = columns.first()): String {
        val sortedData = data[column]!!.sorted()
        return sortedData[sortedData.size / 2]
    }

    fun filter(x: DataFrame = this, column: String, predicate: (String) -> Boolean): DataFrame{
        val dataCopy = HashMap<String, ArrayList<String>>(data)
        var indexToDelete = firstIndexToDelete(x, column, predicate)
        while(indexToDelete != -1){
            dataCopy[column]!!.removeAt(indexToDelete)
            indexToDelete = firstIndexToDelete(x, column, predicate)
        }
        return DataFrame(dataCopy)
    }


    private fun firstIndexToDelete(x: DataFrame, column: String, predicate: (String) -> Boolean): Int{
        return x[column].indexOfFirst{ !predicate(it) }
    }

    override fun equals(other: Any?): Boolean {
        if(other !is DataFrame) return false

        return other.data == this.data
    }
}
