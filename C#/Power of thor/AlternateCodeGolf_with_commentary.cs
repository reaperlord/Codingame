using c = System.Console;

class CodeGolfCommentary_01
{
    static void Main() //get rid of unnecessary args
    {

        int p(string s) => int.Parse(s); //parsing alias

        var i = c.ReadLine().Split(' '); //i is for inputs
        int x, y;
        string e, n;

        x = p(i[0]) - p(i[2]); //difference between light and thor (if light is west of thor, x will be negative
        (x, e) = x < 0 ? (-x, "W") : (x, "E"); //set direction and make x absolute

        y = p(i[1]) - p(i[3]); //if y is negative light is to north of thor
        (y, n) = y < 0 ? (-y, "N") : (y, "S");

        (x, e, n) = x > y ? (y, e, n + e) : (x, n, n + e); //reusing of vars: x becomes counter of joined dirs, e is single dir, n is joined dir

        // game loop
        for (; ; )
        {
            c.ReadLine(); // The remaining amount of turns Thor can move. Do not remove this line.



            // A single line providing the move to be made: N NE E SE S SW W or NW
            c.WriteLine((x-- > 0 ? n : e));
        }
    }
}