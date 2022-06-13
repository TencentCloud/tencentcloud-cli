**Example 1: 查询用户组成员列表**



Input: 

```
tccli dasb DescribeUserGroupMembers --cli-unfold-argument  \
    --Id 1 \
    --Name 张三 \
    --Bound True
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "UserSet": [
            {
                "UserName": "张三",
                "GroupSet": [
                    {
                        "Id": 1,
                        "Name": 1
                    }
                ],
                "RealName": "xx",
                "Email": "xx",
                "Phone": "xx",
                "ValidateTo": "2020-09-22T00:00:00+00:00",
                "ValidateFrom": "2020-09-22T00:00:00+00:00",
                "Id": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

