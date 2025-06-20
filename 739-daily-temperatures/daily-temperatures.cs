public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        int n = temperatures.Length;
        int[] res = new int[n];
        Stack<(int temp, int index)> st = new Stack<(int temp, int index)>();

        for (int i = 0; i < n; i++){
            int temperature = temperatures[i];
            while (st.Count != 0 && temperature > st.Peek().temp){
                var (stTemp, stIndex) = st.Pop();
                res[stIndex] = i - stIndex;
            }
            st.Push((temperature, i));
        }
        return res;
        
    }
}