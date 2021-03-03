**Example 1: 获取反弹Shell规则列表**

获取反弹Shell规则列表

Input: 

```
tccli cwp DescribeReverseShellRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Status": 1,
                "Uuid": "xx",
                "DestIp": "xx",
                "Hostip": "xx",
                "IsGlobal": 1,
                "CreateTime": "xx",
                "ProcessName": "xx",
                "ModifyTime": "xx",
                "Operator": "xx",
                "Id": 1,
                "DestPort": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

