object Solution {
  val letterMap: Map[Char, String] = Map(
    '2' -> "abc", '3' -> "def",
    '4' -> "ghi", '5' -> "jkl", 
    '6' -> "mno", '7' -> "pqrs", 
    '8' -> "tuv", '9' -> "wxyz"
  )

  def letterCombinations(digits: String): List[String] = {    
    if (digits.isEmpty) Nil
    else go(digits.toList).map(_.mkString).toList

  }

  def go(digits: List[Char]): Seq[List[Char]] = {
    digits match {
      case Nil     
        => Seq(Nil) 
      case d :: ds 
        => for {
            c <- letterMap(d)
            rest <- go(ds) 
          } yield c +: rest
    }
  }
}