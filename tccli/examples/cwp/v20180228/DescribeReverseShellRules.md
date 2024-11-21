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
                "Id": 10001,
                "DestIp": "127.0.0.1",
                "Hostip": "10.0.0.11",
                "Uuid": "E86E092B-FD69-4D1B-B014-E4FC68A*****",
                "DestPort": "60132",
                "ProcessName": "python",
                "IsGlobal": 0,
                "Operator": "operatorA",
                "Status": 0,
                "CreateTime": "2024-10-12 11:38:43",
                "ModifyTime": "2024-10-12 11:38:43"
            }
        ],
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

