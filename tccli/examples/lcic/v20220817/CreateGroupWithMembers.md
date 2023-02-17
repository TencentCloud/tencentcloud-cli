**Example 1: 创建群组**

根据成员列表创建群组

Input: 

```
tccli lcic CreateGroupWithMembers --cli-unfold-argument  \
    --GroupName test \
    --SdkAppId 12345678 \
    --MemberIds abc bcd
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

