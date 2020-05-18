using c = System.Console;

class CodeGolfCommentary
{
    static void Main() //get rid of unnecessary args
    {
        
        int p(string s) => int.Parse(s); //parsing alias

        var i = c.ReadLine().Split(' '); //i is for inputs
        int x = p(i[0]), // x is lightX
        y = p(i[1]), // b is lightY
        X = p(i[2]), // X is Thor's starting X position
        Y = p(i[3]); // Y is Thor's starting Y position
        string e = "W", //can be east or west
        n = "N"; //can be north or south

        if (x > X) //if lightX is east of thor        {
            (x, X,e) = (X, x,"E"); //switch vars
        

        if (y > Y) //if light is to south of thor                   
            (y, Y,n) = (Y, y ,"S"); //switch vars
        

        // game loop
        for(;;)
        {
            c.ReadLine(); // The remaining amount of turns Thor can move. Do not remove this line.

            // A single line providing the move to be made: N NE E SE S SW W or NW
            c.WriteLine( (y++ < Y ? n : "") +
                 (x++ < X ? e : "")
                 );
        }
    }
}