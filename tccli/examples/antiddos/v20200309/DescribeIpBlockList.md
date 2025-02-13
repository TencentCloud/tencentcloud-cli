**Example 1: 获取IP封堵列表**



Input: 

```
tccli antiddos DescribeIpBlockList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Status": "1",
                "Ip": "1.1.1.1",
                "UnBlockTime": "2020-09-22 00:00:00",
                "ActionType": "type",
                "BlockTime": "2020-09-22 00:00:00",
                "ProtectFlag": 1
            }
        ],
        "RequestId": "reqid"
    }
}
```

