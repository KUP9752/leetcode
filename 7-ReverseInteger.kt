class Solution {
  fun reverse(x: Int): Int {
    var reverse:Int = 0
    var tempX = x
    var digit:Int


    while (tempX != 0) {
      digit = tempX % 10
      tempX /= 10
      /* Positive Case */
      if (reverse > Int.MAX_VALUE / 10 || (reverse == Int.MAX_VALUE && digit > 7)) 
        return 0
      /* Negative Case */
      if (reverse < Int.MIN_VALUE / 10 || (reverse == Int.MIN_VALUE && digit < -8))
        return 0
      /* Because of the 2s complement (the upper range has - 1) we have to check agaist '> 7' and '< -8' 
         for the positive and negative cases respectively   */
      
      reverse = reverse * 10 + digit
    }

    return reverse

  }
}