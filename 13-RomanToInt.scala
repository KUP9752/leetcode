object Solution {
  def romanToInt(s: String): Int = {
    //define a map witht he predefined values
    val nums: Map[Char, (Int, Set[Char])] = Map(
      'I' -> (1, Set('V', 'X')),
      'V' -> (5, Set()),
      'X' -> (10, Set('L', 'C')),
      'L' -> (50, Set()),
      'C' -> (100, Set('D', 'M')),
      'D' -> (500, Set()),
      'M' -> (1000, Set())
    )


    def romanMatcher(curr: Char, next: Option[Char]): Int = {
      val (v, bef) = nums(curr)
      next match {
        case Some(c) => if (bef.contains(c)) -v else v
        case None    => v 
      }
    }

    /* Matches individual characters, has optional lookahead */
    def accRoman(s: String, acc: Int): Int = {
      s.headOption match {
        //more chars to process 
        case Some(c) => {
          val rem = s.tail
          accRoman(rem, acc + romanMatcher(c, rem.headOption))
        }
        case None    => acc
      }
    }

  



    accRoman(s, 0)
  }
}