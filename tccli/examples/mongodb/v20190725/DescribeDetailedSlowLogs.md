**Example 1: 查询慢日志详情**



Input: 

```
tccli mongodb DescribeDetailedSlowLogs --cli-unfold-argument  \
    --InstanceId cmgo-qny2**** \
    --StartTime 2025-03-27 12:00:00 \
    --EndTime 2025-03-27 13:33:00
```

Output: 
```
{
    "Response": {
        "DetailedSlowLogs": [
            {
                "Log": "xxxxxxx",
                "NodeName": "cmgo-xxxx_0-node-primary",
                "QueryHash": "BA0DFF88"
            }
        ],
        "RequestId": "a1460a2d-dc8e-467c-b2d5-0beb6b84a7a7",
        "TotalCount": 2
    }
}
```

