**Example 1: 聚合子群组创建联合群组**

聚合子群组创建联合群组

Input: 

```
tccli lcic CreateGroupWithSubGroup --cli-unfold-argument  \
    --GroupName test \
    --SdkAppId 12345678 \
    --TeacherId dfgdfg \
    --SubGroupIds abc bcd
```

Output: 
```
{
    "Response": {
        "GroupId": "2CvDgjRNjylAsBZB4iZc0F6koXe",
        "RequestId": "213das"
    }
}
```

