#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int T;
    cin >> T;

    for(int tc = 1; tc <= T; tc++) {
        int people_num;
        cin >> people_num;

        int min_val = 1000000;
        int count = 0;

        for(int i = 0; i < people_num; i++) {
            int x;
            cin >> x;
            int abs_val = abs(x);

            if(abs_val < min_val) {
                min_val = abs_val;
                count = 1;
            }
            else if(abs_val == min_val) {
                count++;
            }
        }

        cout << "#" << tc << " " << min_val << " " << count << endl;
    }

    return 0;
}