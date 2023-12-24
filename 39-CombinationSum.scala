object Solution {
  // def combinationSum(candidates: Array[Int], target: Int): List[List[Int]] = {
  //   val cache: Map[Int, List[List[Int]]] = Map()

  //   def memo(target: Int): List[List[Int]] = {
  //     target match {
  //       case 0 => List(List())
  //       case _ => for {
  //                   x <- candidates.toList
  //                   comb <- cache(x) 
  //                   if (x <= target) 
  //                 }
  //     }
  //   }


  // }
  // def combinationSum(candidates: Array[Int], target: Int): List[List[Int]] = {
  //   val relCands = candidates.filter(_ <= target).toList
  //   val sols = target match {
  //     case 0 => List(List())
  //     case _ => for {
  //                 x <- relCands
  //                 comb <- combinationSum(candidates, target - x)
  //               } yield x :: comb
  //   }
  //   sols.map(_.sorted).distinct
  // }

  def combinationSum(candidates: Array[Int], target: Int): List[List[Int]] = {
    val sols = target match {
      case 0 => List(List())
      case _ => for {
                  x <- candidates.toList
                  if (x <= target)
                  comb <- combinationSum(candidates, target - x)
                } yield x :: comb
    }
    // sols
    sols.map(_.sorted).distinct
  }
}