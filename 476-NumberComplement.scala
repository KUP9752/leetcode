object Solution {
  def findComplement(num: Int): Int = {
    val bin = num.toBinaryString
    val switch = (c: Char) => c match {
      case '0' => 1
      case '1' => 0
      //no other case
    }
    val binAcc = (prev: Int, curr: Int) => prev * 2 + curr * 1
    // println(bin)
    val comp = bin.map(switch(_))
    // println(comp)
    comp.foldLeft(0)(binAcc)
    // println(yeet)
    // 1
  }
}