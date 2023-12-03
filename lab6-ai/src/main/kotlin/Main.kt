import lib.DataFrame
import lib.DecisionTree
import lib.entropy
import kotlin.math.log2


fun main(){
    run()
}



fun run() {
    val df = DataFrame(
        mutableListOf(
            "poisonous",
            "cap-shape", "cap-surface", "cap-color", "bruises", "odor",
            "gill-attachment", "gill-spacing", "gill-size", "gill-color",
            "stalk-shape", "stalk-root", "stalk-surface-above-ring",
            "stalk-surface-below-ring", "stalk-color-above-ring",
            "stalk-color-below-ring", "veil-type", "veil-color", "ring-number",
            "ring-type", "spore-print-color", "population", "habitat"

        )
    )

    df.readFromCSV("src/data/agaricus-lepiota.data")
    val x = df.drop("poisonous")
    val y = df.getColumn("poisonous")
    val tree = DecisionTree(columns = listOf("cap-color", "stalk-color-below-ring", "population", "ring-type", "stalk-shape"))
    tree.fit(x, y)
    tree.print()
}
