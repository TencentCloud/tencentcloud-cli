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
                "Status": "xx",
                "Ip": "xx",
                "UnBlockTime": "2020-09-22 00:00:00",
                "ActionType": "xx",
                "BlockTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

