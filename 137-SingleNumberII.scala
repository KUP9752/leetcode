object Solution {
  def singleNumber(nums: Array[Int]): Int = {
    var once = 0
    var twice = 0

    for (num <- nums) {
      once ^= (num & ~twice)
      twice ^= (num & ~once)
    }
    once
  }
}