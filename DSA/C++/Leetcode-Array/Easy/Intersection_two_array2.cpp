#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> mp;
        vector<int> res;
        for (int v : nums1) mp[v]++;
        for (int v : nums2) {
            if (mp[v] > 0) {
                res.push_back(v);
                mp[v]--;
            }
        }
        return res;
    }
};

int main() {
    vector<int> nums1 = {1, 2, 2, 1};
    vector<int> nums2 = {2, 2};

    Solution sol;
    vector<int> result = sol.intersect(nums1, nums2);

    for (int v : result) {
        cout << v << " ";
    }
    cout << endl;

    return 0;
}
