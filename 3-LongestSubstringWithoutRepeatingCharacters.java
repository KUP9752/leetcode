import java.util.Map;
import java.util.HashMap;

class Solution {
public static int lengthOfLongestSubstring(String s) {
          int res = 0;
        int start = 0;
        int end = 0;
        Map<Character, Integer> charMap = new HashMap<>();

        while (end < s.length()) {
            char c = s.charAt(end);
            if (charMap.containsKey(c)) {
                start = Math.max(start, charMap.get(c));
            }
            res = Math.max(res, end - start + 1);
            charMap.put(c, end + 1);
            end++;
        }
        return res;
    }
}