**Example 1: 创建用户组**

创建用户组

Input: 

```
tccli organization CreateGroup --cli-unfold-argument  \
    --ZoneId z-7cbs6s6gs*** \
    --GroupName testGroup \
    --Description this is group
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
            "GroupId": "g-8sh7baix****",
            "MemberCount": 0
        },
        "RequestId": "e297543a-80de-4039-83c8-9d35d4545"
    }
}
```

