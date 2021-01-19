**Example 1: 查询指定指标的配额使用量**



Input: 

```
tccli tcb DescribeQuotaData --cli-unfold-argument  \
    --EnvId test-23 \
    --MetricName DbWritepkg
```

Output: 
```
{
    "Response": {
        "MetricName": "DbWritepkg",
        "RequestId": "548c46c8-a177-4e39-820a-b544b3fd48c6",
        "Value": 0,
        "SubValue": "100"
    }
}
```

