object Solution {
  def generate(numRows: Int): List[List[Int]] = {
    def go(rows: Int): List[List[Int]]
      = rows match {
        case 1 => List(List(1))
        case 2 => List(List(1, 1), List(1))
        case x => {
          val prev  = x - 1
          val prevs@(head :: _) = go(prev)

          println(prevs)
          println(head.size)

          var mid = List(1)
          for {
            i <- (0 to x - 3)
          } mid = (head(i) + head(i + 1)) :: mid
          // yield (head(i) + head(j))
          //println(s"i${head(i)} j${head(j)} +${head(i) + head(j)}")
          
          (1 :: mid) :: prevs
        }
      }
    go(numRows).reverse
  }
}