**Example 1: 批量创建群组**

批量创建群组

Input: 

```
tccli lcic BatchCreateGroupWithMembers --cli-unfold-argument  \
    --SdkAppId 12345678 \
    --GroupBaseInfos.0.GroupName test1 \
    --GroupBaseInfos.0.TeacherId abc \
    --GroupBaseInfos.1.GroupName test2 \
    --MemberIds abc bcd
```

Output: 
```
{
    "Response": {
        "GroupIds": [
            "2CvDgjRNjylAsBZB4iZc0F6koXe",
            "abcddredrtertet"
        ],
        "RequestId": "213das"
    }
}
```

