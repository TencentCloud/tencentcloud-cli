**Example 1: 创建群组**

根据成员列表创建群组

Input: 

```
tccli lcic CreateGroupWithMembers --cli-unfold-argument  \
    --GroupName Group_name \
    --SdkAppId 3450918 \
    --MemberIds member_1 member_2
```

Output: 
```
{
    "Response": {
        "GroupId": "2CvDgjRNjylAsBZB4iZc0F6koXe",
        "RequestId": "bb9c8d-4236-419b-8c39-572234jifsns7"
    }
}
```

