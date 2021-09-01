**Example 1: 查询告警历史**



Input: 

```
tccli tke DescribePrometheusAlertHistory --cli-unfold-argument  \
    --InstanceId prom-xxx \
    --RuleName xxx
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Content": "xx",
                "StartTime": "xx",
                "RuleName": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

