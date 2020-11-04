**Example 1: 获取反弹Shell规则列表**

获取反弹Shell规则列表

Input: 

```
tccli yunjing DescribeReverseShellRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 5,
        "List": [
            {
                "Id": 2,
                "Uuid": "6b13beb4-be6e-11e9-a040-40f2e9f5c7d2",
                "ProcessName": "first233",
                "DestIp": "127.0.0.1",
                "DestPort": "8080",
                "Operator": "console",
                "IsGlobal": 0,
                "Status": 0,
                "CreateTime": "2019-08-23 16:08:58",
                "ModifyTime": "2019-08-23 16:08:58"
            }
        ],
        "RequestId": "b12a5e5a-9393-453f-a4d9-b42de0b2bcec"
    }
}
```

