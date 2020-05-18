using System;

    class Player
    {
        static void Main(string[] args)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            int lightX = int.Parse(inputs[0]); // the X position of the light of power
            int lightY = int.Parse(inputs[1]); // the Y position of the light of power
            int initialTx = int.Parse(inputs[2]); // Thor's starting X position
            int initialTy = int.Parse(inputs[3]); // Thor's starting Y position


            string xDir = "W", yDir = "N";

            if (lightX > initialTx) //if lightX is east of thor
            {
                xDir = "E";
                (lightX, initialTx) = (initialTx, lightX);
            }

            if (lightY > initialTy) //if light is to south of thor
            {
                yDir = "S";
                (lightY, initialTy) = (initialTy, lightY);
            }

            // game loop
            while (true)
            {
                Console.ReadLine(); // The remaining amount of turns Thor can move. Do not remove this line.



                // A single line providing the move to be made: N NE E SE S SW W or NW
                Console.WriteLine((lightY++ < initialTy ? yDir : "") +
                     (lightX++ < initialTx ? xDir : "") 
                     );
            }
        }
    }

