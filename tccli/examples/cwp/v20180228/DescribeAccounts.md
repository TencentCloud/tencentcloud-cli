**Example 1: 获取帐号列表**

获取帐号列表

Input: 

```
tccli cwp DescribeAccounts --cli-unfold-argument  \
    --Username nginx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Accounts": [
            {
                "Id": 1,
                "Uuid": "6b6cd843-6bc1-4011-a74c-dc3fd26a7dd1",
                "MachineIp": "10.12.12.14",
                "MachineName": "machine-name",
                "Username": "nginx",
                "Groups": "users",
                "Privilege": "ORDINARY",
                "AccountCreateTime": "2018-01-01 12:12:12",
                "LastLoginTime": "2018-01-01 12:12:12"
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100
    }
}
```

