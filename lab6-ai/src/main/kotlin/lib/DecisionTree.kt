package lib

import kotlin.system.exitProcess

class DecisionTree(
    private val columns: List<String>
) {


    private lateinit var root: AbstractNode

    fun fit(x: DataFrame, y: DataFrame){
        root = addNode(x[columns], y, entropy(y.first().distinct()))
    }

    private fun addNode(x: DataFrame, y: DataFrame, parentInfo: Double): AbstractNode{

        if(y[y.columns.first()].distinct().size == 1)
            return LeafNode(y.first()[0], 1.0)


        val (bestGainInfo, bestGainColumn) = chooseColumn(x, y, parentInfo)

        if(bestGainColumn == null){
            val mode = y.mode()
            return LeafNode(mode, y.first().count { it == mode } / y.size.toDouble() )
        }

        val nodes = arrayListOf<AbstractNode>()
        val categories = x[bestGainColumn].distinct()
        println(categories)
        for(category in categories){
            nodes.add(
                addNode(
                    x.filter(column = bestGainColumn){
                      cat: String -> cat == category
                    },
                    y.filter(x, column = bestGainColumn){
                        cat: String -> cat == category
                    },
                    bestGainInfo
                )
            )
        }

        return Node(bestGainColumn, nodes)
    }


    private fun chooseColumn(x: DataFrame,y: DataFrame, parentInfo: Double): Pair<Double, String?> {
        var bestGainValue = 0.0
        var bestGainColumn: String? = null
        var bestGainInfo = 0.0

        for(column in columns){
            val categories = x[column].distinct()
            var info = 0.0

            for(category in categories){
                val weight = x[column].count { it == category } / x.size

                val entropy = ArrayList<String>()
                    .apply{
                        x[column].forEachIndexed{ index: Int, v: String ->
                            if(v == category)
                                this.add(y.first()[index])
                        }
                    }.let {
                        entropy(it)
                    }

                info += entropy * weight
            }

            if(parentInfo - info > bestGainValue){
                bestGainValue = parentInfo - info
                bestGainInfo = info
                bestGainColumn = column
            }
        }
        return bestGainInfo to bestGainColumn
    }

    fun print(){
        root.printNode()
    }

    private abstract class AbstractNode{

        abstract fun printNode(indent: Int = 0)
    }


    private inner class Node(val column: String, val nodes: List<AbstractNode>): AbstractNode() {
        override fun printNode(indent: Int) {
            for(node in nodes){
                println("${" " * indent} $column")
                node.printNode(indent + 2)
            }

        }
    }

    private inner class LeafNode(val value: String, val probability: Double): AbstractNode() {
        override fun printNode(indent: Int) {
            println("${" " * indent} -> $value ($probability)")
        }
    }
}

private operator fun String.times(number: Int): String {
    val builder = StringBuilder()
    repeat(number){
        builder.append(this)
    }
    return builder.toString()
}
