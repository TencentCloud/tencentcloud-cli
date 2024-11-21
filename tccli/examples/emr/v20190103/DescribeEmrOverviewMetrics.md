**Example 1: 查询监控概览页指标数据**



Input: 

```
tccli emr DescribeEmrOverviewMetrics --cli-unfold-argument  \
    --End 1730753724 \
    --Metric NODE.CPU \
    --InstanceId emr-hvijzo6n \
    --Downsample 30s-min
```

Output: 
```
{
    "Response": {
        "RequestId": "a16d3814-3b85-498a-97a7-15e7b0f0f0bd",
        "Result": [
            {
                "Metric": "EMR.19003289.NODE.CPU",
                "Tags": {
                    "Type": "CPUUsedPercent"
                },
                "First": 1730148930,
                "Last": 1730753700,
                "Interval": 30,
                "DataPoints": [
                    "2.3",
                    "2.4",
                    "2.6",
                    "3.8",
                    "2.8",
                    "3.1",
                    "3.4",
                    "3.3",
                    "3.6",
                    "4.3",
                    "3",
                    "3.1",
                    "2.3",
                    "2.9",
                    "2.5",
                    "2.4",
                    "2.2",
                    "4.1",
                    "3.3",
                    "2.5",
                    "4.5",
                    "4.7",
                    "2.5",
                    "3.6",
                    "2.2",
                    "2.3",
                    "2.5",
                    "2.9",
                    "2.2"
                ]
            },
            {
                "Metric": "EMR.19003289.NODE.CPU",
                "Tags": {
                    "Type": "CPUCoresTotal",
                    "Unit": "核"
                },
                "First": 1730148930,
                "Last": 1730753700,
                "Interval": 30,
                "DataPoints": [
                    "118"
                ]
            }
        ]
    }
}
```

