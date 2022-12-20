**Example 1: 查询Prometheus按量实例用量**



Input: 

```
tccli monitor DescribePrometheusInstanceUsage --cli-unfold-argument  \
    --InstanceIds prom-xxxxx \
    --StartCalcDate 20210101 \
    --EndCalcDate 20210101
```

Output: 
```
{
    "Response": {
        "UsageSet": [
            {
                "InstanceId": "prom-xxxxx",
                "CalcDate": "20210101",
                "Total": 1.1,
                "Basic": 1.1,
                "Fee": 1.1
            }
        ],
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

