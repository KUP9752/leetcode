object Solution {
  def missingNumber(nums: Array[Int]): Int = {
    val bitmap: List[Boolean] = List.tabulate(nums.length + 1)(_ => false)

    for {
      x <- nums
      bitmap(x) = true
    }

    println(bitmap)
    return 0

  }
}