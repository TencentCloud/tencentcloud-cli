**Example 1: 查询用户组信息**

查询用户组信息

Input: 

```
tccli organization GetGroup --cli-unfold-argument  \
    --ZoneId z-ws9sdj8**** \
    --GroupId g-sushsia7s8
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
            "GroupId": "g-sushsia7s8",
            "MemberCount": 20
        },
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

