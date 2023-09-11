int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize = 2;
    // 初始化ret, 宣告i,j
    int *ret = (int*)malloc(2*sizeof(int)),i,j;
    for (int i=0;i<numsSize-1;i++){
        for (int j=i+1;j<numsSize;j++){
            if (nums[i] + nums[j] == target){
                ret[0] = i;
                ret[1] = j;
                return ret;
            }
        }
    }
    return ret;
}