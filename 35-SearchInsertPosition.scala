object Solution {

  
  lazy val splitter = (xs: Array[Int], i: Int) => (xs.take(i), xs.drop(i))

  def searchInsert(nums: Array[Int], target: Int): Int = {
    nums match {
      case Array(x) if (target <= x) => 0
      case Array(x) if (target > x)  => 1
      case _ 
      => {
        val mid = nums.length / 2
        val (first, rest @ Array(pivot, _*)) = splitter(nums, mid)
        // if (target == pivot) mid
        if (target <= pivot) searchInsert(first, target)
        else mid + searchInsert(rest, target)
      }
    }
  }
}