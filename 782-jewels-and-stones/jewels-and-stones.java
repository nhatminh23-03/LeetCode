class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        /*int count = 0;
        
        for (int i = 0; i < stones.length(); i++){
            for (int j = 0; j < jewels.length(); j++){
                if (stones.charAt(i) == jewels.charAt(j)){
                    count++;
                    break;
                }
            }
        }
        
        return count;*/ // O(n*m)
        
        // O(m + n)
        
        Set<Character> jewelsSet = new HashSet<>();
        for (int i = 0; i < jewels.length(); i++){
            jewelsSet.add(jewels.charAt(i));
        }
        
        int count = 0;
        for (int i = 0; i < stones.length(); i++){
            if(jewelsSet.contains(stones.charAt(i))){
                count++;
            }
        }
        return count;
        
    }
}