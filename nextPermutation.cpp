#include <bits/stdc++.h> 
using namespace std;
vector<int> nextPermutation(vector<int> &permutation, int n)
{
    //  Write your code here.
    next_permutation(permutation.begin(),permutation.end());
    return permutation;
}