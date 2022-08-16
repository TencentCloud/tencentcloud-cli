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
                "UserName": "xx",
                "AuthType": 1,
                "ValidateTo": "2020-09-22T00:00:00+00:00",
                "RealName": "xx",
                "ValidateTime": "xx",
                "Email": "xx",
                "Phone": "xx",
                "GroupSet": [
                    {
                        "Department": {
                            "Managers": [
                                "xx"
                            ],
                            "Id": "xx",
                            "Name": "xx"
                        },
                        "Id": 1,
                        "Name": "xx"
                    }
                ],
                "DepartmentId": "xx",
                "Department": {
                    "Managers": [
                        "xx"
                    ],
                    "Id": "xx",
                    "Name": "xx"
                },
                "ValidateFrom": "2020-09-22T00:00:00+00:00",
                "Id": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

