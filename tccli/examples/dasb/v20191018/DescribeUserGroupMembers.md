**Example 1: 查询用户组成员列表**



Input: 

```
tccli dasb DescribeUserGroupMembers --cli-unfold-argument  \
    --Id 1 \
    --Name 张三 \
    --Bound True \
    --Offset 1 \
    --Limit 1 \
    --DepartmentId 1.4
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "UserSet": [
            {
                "UserName": "Aiden",
                "AuthType": 1,
                "ValidateTo": "2020-09-22T00:00:00+08:00",
                "RealName": "Henry",
                "ValidateTime": "2020-09-22T00:00:00+08:00",
                "Email": "245***106@163.com",
                "Phone": "177****4532",
                "GroupSet": [
                    {
                        "Department": {
                            "Managers": [
                                "457824365"
                            ],
                            "Id": "10",
                            "Name": "测试组"
                        },
                        "Id": 1,
                        "Name": "开发组",
                        "Count": 1
                    }
                ],
                "DepartmentId": "1.5",
                "Department": {
                    "Managers": [
                        "15478952664"
                    ],
                    "Id": "231",
                    "Name": "测试组"
                },
                "ValidateFrom": "2020-09-22T00:00:00+00:00",
                "Id": 1
            }
        ],
        "RequestId": "557246f9-3ee4-406d-8c36-6885e2ae52d9"
    }
}
```

