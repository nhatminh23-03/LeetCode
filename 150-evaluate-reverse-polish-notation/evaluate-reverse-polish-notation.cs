public class Solution {
    public int EvalRPN(string[] tokens) {
        Stack<int> st = new Stack<int>();

        foreach (string c in tokens){
            if (c == "+"){
                int first = st.Pop();
                int second = st.Pop();
                int addition = first + second;
                st.Push(addition);
            } else if (c == "-"){
                int first = st.Pop();
                int second = st.Pop();
                int sub = second - first;
                st.Push(sub);
            } else if (c == "*"){
                int first = st.Pop();
                int second = st.Pop();
                int mult = first * second;
                st.Push(mult);
            } else if (c == "/"){
                int first = st.Pop();
                int second = st.Pop();
                int division = 0;
                if (second == 0){
                    division = 0;
                } else {
                    division = second / first;
                }
                st.Push(division);
            } else {
                st.Push(int.Parse(c));
            }
        }
        return st.Peek();
        
    }
}