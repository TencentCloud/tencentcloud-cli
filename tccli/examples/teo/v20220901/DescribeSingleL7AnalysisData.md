**Example 1: 查询七层数据分析类单值流量数据**



Input: 

```
tccli teo DescribeSingleL7AnalysisData --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Flow_singleIpRequest
```

Output: 
```
{
    "Response": {
        "RequestId": "4f9b86cc-d62b-4a69-a640-52f6f3cb628e",
        "Data": [
            {
                "TypeKey": "251227260",
                "TypeValue": [
                    {
                        "DetailData": 65,
                        "MetricName": "l7Flow_singleIpRequest"
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

