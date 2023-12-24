import scala.collection.mutable.{MutableList => MutList}

class MinStack() {
  private val stack = MutList[(Int, Int)]()

  def push(value: Int) {
    (v, m) = if (stack.isEmpty) (value, value) else (value, stack.last._2)  
    stack += (v, m)
  }

  def pop() = stack = stack.dropRight(1)

  def top(): Int = {
    stack.remove()
  }

  def getMin(): Int = {
      
  }

}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(`val`)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */