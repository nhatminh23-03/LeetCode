public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        List<string> result = new List<string>();
        Stack<char> stack = new Stack<char>();

        void backTracking(int openN, int closeN){
            if (openN == n && closeN == n){
                result.Add(new String(stack.Reverse().ToArray()));
                return;
            }
            if (openN < n){
                stack.Push('(');
                backTracking(openN + 1, closeN);
                stack.Pop();
            }
            if (closeN < openN){
                stack.Push(')');
                backTracking(openN, closeN + 1);
                stack.Pop();
            }
        }
        backTracking(0,0);
        return result;
        
    }
}