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
                "UserName": "xx",
                "AuthType": 1,
                "ValidateTo": "2020-09-22T00:00:00+00:00",
                "RealName": "xx",
                "Email": "xx",
                "Phone": "xx",
                "GroupSet": [
                    {
                        "Id": 1,
                        "Name": "xx"
                    }
                ],
                "ValidateFrom": "2020-09-22T00:00:00+00:00",
                "Id": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

**Example 2: 根据主机查询有访问权限的用户信息**

根据主机查询有访问权限的用户信息

Input: 

```
tccli dasb DescribeUsers --cli-unfold-argument  \
    --AuthorizedDeviceIdSet 63 64 82 100 \
    --Name u
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
                "Email": "xx",
                "Phone": "xx",
                "GroupSet": [
                    {
                        "Id": 1,
                        "Name": "xx"
                    }
                ],
                "ValidateFrom": "2020-09-22T00:00:00+00:00",
                "Id": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

