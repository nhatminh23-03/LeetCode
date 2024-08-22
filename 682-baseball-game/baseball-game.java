class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> newStack = new Stack<>();
        
        for (int i = 0; i < operations.length; i++){
            String s = operations[i];
            
            if (s.equals("+")){
                int top = newStack.pop();
                int sum = top + newStack.peek();
                newStack.push(top);
                newStack.push(sum);
            } else if (s.equals("D")){
                newStack.push(newStack.peek() * 2);
            } else if (s.equals("C")){
                newStack.pop();
            } else {
                newStack.push(Integer.parseInt(s));
            }
        }
        
        int sum = 0;
        for (int i = 0; i < newStack.size();i++){
            sum += newStack.get(i);
        }
        
        return sum;
        
    }
}