object Solution {
  def arraySign(nums: Array[Int]): Int = {
    var prod = 1
    nums.foreach(n => {
      prod = n match {
        case 0              => return 0
        case x if (x <= -1) => - prod
        case _              => prod
      }
    })
    prod
  }
}