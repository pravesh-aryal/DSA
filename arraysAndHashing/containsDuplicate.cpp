#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;
bool hasDuplicate(std::vector<int> &nums){
    std::unordered_set<int> uniqueNums;

    for (int num: nums){
        if (uniqueNums.count(num)){
            return true;
        }
        uniqueNums.insert(num);
    }
    return false;
}


int main(){
    std::vector<int> nums = {1, 2, 3, 4,5, 1};

    if (hasDuplicate(nums)){
        cout << "The list has duplicate" << endl;
    }else{
        cout << "The list does not have duplicate" << endl;
    }
}