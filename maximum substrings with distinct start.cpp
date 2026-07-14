#include <string>
#include <unordered_set>
using namespace std;


class Solution {
public:
    int maxDistinct(string s) {
        unordered_set<char> chars;
        for (char c : s) {
            chars.insert(c);
        }
        return chars.size();
    }
};
    
