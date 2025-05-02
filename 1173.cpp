#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        long long x;
        cin >> n >> x;
        
        for (int i = 0; i < n; ++i) {
            int num;
            cin >> num;
            if (num <= x) {
                x += num;
            }
        }
        
        cout << x << '\n';
    }
    
    return 0;
}