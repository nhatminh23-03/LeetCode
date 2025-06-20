public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        int n = position.Length;
        if (n == 0) return 0;

        var cars = new (int pos, double time)[n];
        for (int i = 0; i < n; i++){
            double time = (double)(target - position[i]) / speed[i];
            cars[i] = (position[i], time);
        }
        Array.Sort(cars, (a,b)=>b.pos.CompareTo(a.pos));

        Stack<double> st = new Stack<double>();

        foreach(var car in cars){
            if (st.Count == 0 || car.time > st.Peek()){
                st.Push(car.time);
            }
        }
        return st.Count;
    }
}