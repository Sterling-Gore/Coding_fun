#include <iostream>

int main()
{
    int n, s, m;
    std::cin >> n >> s >> m;
    // n is the number of squares on the board
    // s is the starting square using 1-index   (we'll fix that)
    // m is the target value that we want to reach
    s--;
    int *board = new int[n];
    int *visited_board = new int[n];

    for (int i = 0; i < n; i++)
    {
        std::cin >> board[i];
        visited_board[i] = 0;
    }

    int count = 0;

    while (true)
    {
        if (s >= n)
        {
            std::cout << "right" << std::endl;
            break;
        }
        else if (s < 0)
        {
            std::cout << "left" << std::endl;
            break;
        }
        else if (board[s] == m)
        {
            // this means we hit our magic number
            std::cout << "magic" << std::endl;
            break;
        }
        else if (visited_board[s] == 1)
        {
            std::cout << "cycle" << std::endl;
            break;
        }

        visited_board[s] = 1;
        s += board[s];
        count++;
    }
    std::cout << count << std::endl;

    delete[] board;
    delete[] visited_board;

    return 0;
}