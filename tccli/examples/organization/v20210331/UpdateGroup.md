**Example 1: 修改用户组信息**

修改用户组信息

Input: 

```
tccli organization UpdateGroup --cli-unfold-argument  \
    --ZoneId z-s8shs8bd*** \
    --GroupId g-s8dhdn3 \
    --NewGroupName testGroup \
    --NewDescription this is group.
```

Output: 
```
{
    "Response": {
        "GroupInfo": {
            "GroupName": "testGroup",
            "Description": "this is group",
            "CreateTime": "2024-01-01 12:12:12",
            "GroupType": "Manual",
            "UpdateTime": "2024-01-01 12:12:12",
            "GroupId": "g-w8hd8n***",
            "MemberCount": 20
        },
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

