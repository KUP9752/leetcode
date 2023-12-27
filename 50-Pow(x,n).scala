object Solution {
    def myPow(x: Double, n: Int): Double = {
      n match {
        case 0 => 1.0
        case 1 => x
        case -1 => 1.0 / x
        case _  => {
          val halfPow = myPow(x, n / 2)
          val pow = halfPow * halfPow
          // if (n % 2 == 0) pow
          // else pow * myPow(x, n % 2)
          pow * myPow(x, n % 2)
        }
      }
        
    }
}


object Main {
  def main(args: Array[String]): Unit = {
    val ans = Solution.myPow(2.4, 5)
    println(s"ans =  $ans")
  }
}