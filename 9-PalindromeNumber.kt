import kotlin.math.*
class Solution {
  fun isPalindrome(x: Int): Boolean {
    /* Negative numbers are non-palindromes by definition */
    if (x < 0) return false
    /* if the last digit is a 0, so must be the first -> only 0 works */
    if (x % 10 == 0 && x != 0) return false

    /* Revert half the number */
    var reverse = 0
    var tempX = x
    while (tempX > reverse) {
      reverse = reverse * 10 + tempX % 10
      tempX /= 10
  
    }
    return tempX == reverse || tempX == reverse / 10
  }
}