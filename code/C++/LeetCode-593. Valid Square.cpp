class Solution {
public:

    int lengths(vector<int>& a,vector<int>&b)
    {
        return (a[0]-b[0]) * (a[0]-b[0]) + (a[1]-b[1]) * (a[1]-b[1]);
    }
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) 
    {
        unordered_set<int> myset({lengths(p1,p2), lengths(p1,p3), lengths(p1,p4), lengths(p2,p3), lengths(p2,p4), lengths(p3,p4)});
        return !myset.count(0) && myset.size() == 2;
    }
};
