class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> magazineMap = new HashMap<>();
        
        char[] magazineArray = magazine.toCharArray();
        for (int i = 0; i < magazineArray.length; i++){
            char c = magazineArray[i];
            magazineMap.put(c, magazineMap.getOrDefault(c,0) + 1);
        }
        
        char[] ransomArray = ransomNote.toCharArray();
        for (int i = 0; i < ransomArray.length; i++){
            char c = ransomArray[i];
            if (!magazineMap.containsKey(c) || magazineMap.get(c) == 0){
                return false;
            }
            magazineMap.put(c, magazineMap.get(c) - 1);
        }
        return true;
        
    }
}