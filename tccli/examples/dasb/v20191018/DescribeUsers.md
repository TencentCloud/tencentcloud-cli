**Example 1: 查询用户列表**

查询用户列表

Input: 

```
tccli dasb DescribeUsers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "UserSet": [
            {
                "UserName": "jassls",
                "AuthType": 1,
                "ValidateTo": "2020-09-22T00:00:00+00:00",
                "RealName": "张宏宇",
                "ValidateTime": "2020-09-23T00:00:00+00:00",
                "Email": "xxx@tencent.com",
                "Phone": "+86|13500000001",
                "GroupSet": [
                    {
                        "Department": {
                            "Managers": [
                                "152017423"
                            ],
                            "Id": "1.2",
                            "Name": "研发部"
                        },
                        "Id": 1,
                        "Name": "运维组",
                        "Count": 1
                    }
                ],
                "Department": {
                    "Managers": [
                        "152017423"
                    ],
                    "Id": "1.2",
                    "Name": "研发部"
                },
                "ValidateFrom": "2020-09-22T00:00:00+00:00",
                "Id": 1
            }
        ],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

**Example 2: 根据主机查询有访问权限的用户信息**

根据主机查询有访问权限的用户信息

Input: 

```
tccli dasb DescribeUsers --cli-unfold-argument  \
    --AuthorizedDeviceIdSet 63 64 82 100 \
    --Name zhanghongyu
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "UserSet": [
            {
                "UserName": "jassls",
                "AuthType": 1,
                "ValidateTo": "2020-09-22T00:00:00+00:00",
                "RealName": "张宏宇",
                "ValidateTime": "2020-09-23T00:00:00+00:00",
                "Email": "xxx@tencent.com",
                "Phone": "+86|13500000001",
                "GroupSet": [
                    {
                        "Department": {
                            "Managers": [
                                "152017423"
                            ],
                            "Id": "1.2",
                            "Name": "研发部"
                        },
                        "Id": 1,
                        "Name": "运维组",
                        "Count": 1
                    }
                ],
                "Department": {
                    "Managers": [
                        "152017423"
                    ],
                    "Id": "1.2",
                    "Name": "研发部"
                },
                "ValidateFrom": "2020-09-22T00:00:00+00:00",
                "Id": 1
            }
        ],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

