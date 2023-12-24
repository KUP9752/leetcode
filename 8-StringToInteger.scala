object Solution {
  
  def myAtoi(s: String): Int = {
    val two_31 = Math.pow(2, 31).intValue
    val maxINT = Int.MaxValue
    val minINT = Int.MinValue
    //converter helper (foldl)
    val remSpaces = s.dropWhile(c => c == ' ')
    var ret: Int = 0
    var zero: Boolean = false
    val (str, neg) = remSpaces.headOption match {
      case Some('-') => (remSpaces.tail, true) 
      case Some('+') => (remSpaces.tail, false)
      case Some(_)   => (remSpaces, false)
      case None      => {
        zero = true
        (s, false) 
      }
    }
    def conv(s: String): Int= {
      def convHelp(s: String, prev: Long): Long = {
        val add = (x: Long, y: Long) => if (neg) x - y else x + y
        val cmp = (next: Long) => if (neg) (next < minINT, minINT) else (next > maxINT, maxINT)
        
        s.headOption match {
          case Some(c) if (c.isDigit) => {
            val next = add(prev * 10, c.asDigit)

            cmp(next) match {
              case (true, bound) => bound
              case _ => convHelp(s.tail, next)
            }
          }
          case _ => prev
        }
      }

      val noLeading0 = s.dropWhile(c => c == '0')
      convHelp(noLeading0, 0).toInt
    }

    
    if (zero) 0
    else conv(str)

  
    // (zero, neg) match {
    //   case (true, _) => 0
    //   case (_, true) => (- ret).max(minINT)
    //   case _         => ret.min(maxINT)
    // }
  }
}
