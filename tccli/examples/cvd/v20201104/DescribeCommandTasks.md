**Example 1: DescribeCommandTasks**



Input: 

```
tccli cvd DescribeCommandTasks --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Total": 1,
        "Status": "FINISHED",
        "CommandDetails": [
            {
                "Uin": "100000077643",
                "AppId": 13846212,
                "Status": "RUNNING",
                "Command": "aXBjb25maWc",
                "CommandId": "ac5b1e88-9862-423e-9595-10f2998096b5",
                "CreateTime": "2025-04-22 14:01:23",
                "Invocations": []
            }
        ]
    }
}
```

