**Example 1: 查询用户组成员列表**



Input: 

```
tccli bh DescribeUserGroupMembers --cli-unfold-argument  \
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
                "UserName": "zhangsan",
                "AuthType": 1,
                "ValidateTo": "2022-12-31T00:00:00+00:00",
                "RealName": "Zhang San",
                "ValidateTime": "2021-01-01T00:00:00+00:00",
                "Email": "zhangsan@example.com",
                "Phone": "1982****",
                "GroupSet": [
                    {
                        "Department": {
                            "Managers": [
                                "Li Si"
                            ],
                            "Id": "dept01",
                            "Name": "Sales"
                        },
                        "Id": 1,
                        "Name": "Sales Team",
                        "Count": 1
                    }
                ],
                "DepartmentId": "dept01",
                "Department": {
                    "Managers": [
                        "zhangsan"
                    ],
                    "Id": "1.2",
                    "Name": "Sales"
                },
                "ValidateFrom": "2021-01-01T00:00:00+00:00",
                "Id": 1
            }
        ],
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

