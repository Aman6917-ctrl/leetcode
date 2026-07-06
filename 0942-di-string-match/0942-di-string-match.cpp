class Solution {
public:
    vector<int> diStringMatch(string s) {
        vector<int> ans;
        int i = 0;
        int j = s.size();

        for (char ch : s) {
            if (ch == 'I') {
                ans.push_back(i); // smallest available number
                i++;
            }
            else {
                ans.push_back(j); // largest available number
                j--;
            }
        }

        ans.push_back(j); // last remaining number
        return ans;
    }
};