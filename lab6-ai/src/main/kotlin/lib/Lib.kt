package lib

import kotlin.math.log2

fun entropy(x: List<String>): Double {
    var entropy = 0.0
    x.distinct().forEach {
        val p = x.count { value -> value == it } / x.size.toDouble()
        entropy -= p * log2(p)
    }
    return entropy
}