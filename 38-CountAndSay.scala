object Solution {
    def countAndSay(n: Int): String = {
      n match{
        case 1 => "1"
        case _ => say(countAndSay(n - 1))
      }
    }
    def say(seq: String): String = {
      var said: String = ""
      var rem = seq

      while (rem.length != 0) {
        val head = rem.head
        val repeats = rem.takeWhile(_ == head).length
        said = said ++ s"$repeats$head"
        rem = rem.drop(repeats)
      }
      said
    }
}