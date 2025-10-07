#include <iostream>
#include <vector>

void islandPreimeter(std::vector<std::vector<int>>& grid){
    int rows = grid.size();
    int cols = grid[0].size();  
    int perimiter = 0;

    for (int i = 0 ; i < rows; i++){

        for (int j = 0; j < cols; j++ ){

            if(grid[i][j] != 0){
                perimiter +=4;
                if( i > 0 && grid[i-1][j] == 1) perimiter -=2;
                if( j > 0 && grid[i][j-1] == 1) perimiter  -= 2; 
            }
        }
   
    }

    std::cout << perimiter;

}
/*
প্রতিটা ঘরের চারটা দেয়াল মানে ৪টা লাইন 👉 তাই প্রথমে ৪ যোগ করবো।

কিন্তু যদি এই ঘরের পাশে (উপরে বা বামে) আরেকটা ঘর থাকে,
তাহলে তারা একটা দেয়াল share করে ফেলেছে!
মানে ওই দেয়ালটা দুইবার গোনা ঠিক না 😅

তাই প্রতিটা shared দেয়ালের জন্য ২ কমিয়ে দিই।
(একবার ওই ঘরের জন্য, একবার পাশের ঘরের জন্য)
*/



int main(){
    std::vector<std::vector<int>> grid =  {
        {0, 1, 0, 0},
        {1, 1, 1, 0},
        {0, 1, 0, 0},
        {1, 1, 0, 0}
    };

    islandPreimeter(grid);


    return 0;
}