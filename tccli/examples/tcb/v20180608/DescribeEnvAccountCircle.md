**Example 1: 查询环境账单周期**



Input: 

```
tccli tcb DescribeEnvAccountCircle --cli-unfold-argument  \
    --EnvId yntest-1gudy58n050fbe21
```

Output: 
```
{
    "Response": {
        "EndTime": "2025-12-30 23:59:59",
        "RequestId": "5abb2182-a465-412e-b42d-d643ebbd94a4",
        "StartTime": "2025-11-30 00:00:00"
    }
}
```

