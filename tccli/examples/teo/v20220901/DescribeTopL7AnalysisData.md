**Example 1: 查询七层数据分析类top流量数据**



Input: 

```
tccli teo DescribeTopL7AnalysisData --cli-unfold-argument  \
    --Area mainland \
    --Interval day \
    --Limit 1 \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --MetricName l7Flow_outFlux_url
```

Output: 
```
{
    "Response": {
        "RequestId": "7c499897-8ad9-4a2d-884e-6154f283d7f6",
        "Data": [
            {
                "DetailData": [
                    {
                        "Key": "/",
                        "Value": 7410001
                    }
                ],
                "TypeKey": "251227260"
            }
        ],
        "TotalCount": 1
    }
}
```

