class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder newStr = new StringBuilder();
        int i = 0;
        
        while (i < word1.length() || i < word2.length()){
            if (i < word1.length()){
                newStr.append(word1.charAt(i));
            }
            
            if (i < word2.length()){
                newStr.append(word2.charAt(i));
            }
            i++;
        }
        
        return newStr.toString();
        
    }
}