import scala.collection.mutable.Stack 
object Solution {
  def evalRPN(tokens: Array[String]): Int = {
    val stack = Stack()
    val ops = "+-*/"
    val opMap: Map[String, (Int, Int) => Int] 
      = Map(
          "+" -> ((x: Int, y: Int) => x + y),
          "-" -> ((x: Int, y: Int) => x - y),
          "*" -> ((x: Int, y: Int) => x * y),
          "/" -> ((x: Int, y: Int) => x / y)
        )

    for (c <- tokens) {
      if (ops.contains(c)) {
        val op2 = stack.pop.toInt
        val op1 = stack.pop.toInt
        stack.push(opMap(c)(op1, op2))
      } else stack.push(c)
    }
    stack.pop
  }
}