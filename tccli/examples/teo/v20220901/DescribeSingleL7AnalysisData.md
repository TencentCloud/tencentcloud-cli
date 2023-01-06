**Example 1: 查询七层流量分析单值数据**



Input: 

```
tccli teo DescribeSingleL7AnalysisData --cli-unfold-argument  \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
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

**Example 2: 根据HTTP协议查询流量分析单值数据**



Input: 

```
tccli teo DescribeSingleL7AnalysisData --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Flow_singleIpRequest \
    --Filters.0.Key protocol \
    --Filters.0.Operator equals \
    --Filters.0.Value HTTP/1.0 HTTP/1.1 HTTP/2.0 HTTP/3
```

Output: 
```
{
    "Response": {
        "RequestId": "7672fcf7-2e69-478d-85a4-6b980ce5882f",
        "Data": [
            {
                "TypeKey": "1310708577",
                "TypeValue": [
                    {
                        "DetailData": 77,
                        "MetricName": "l7Flow_singleIpRequest"
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 3: 根据标签查询流量分析单值数据**



Input: 

```
tccli teo DescribeSingleL7AnalysisData --cli-unfold-argument  \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --Interval day \
    --Area mainland \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --MetricNames l7Flow_singleIpRequest \
    --Filters.0.Key tagKey \
    --Filters.0.Operator equals \
    --Filters.0.Value test \
    --Filters.1.Key tagValue \
    --Filters.1.Operator equals \
    --Filters.1.Value a.com b.com
```

Output: 
```
{
    "Response": {
        "RequestId": "962792de-3bfe-483d-99a7-3cfde0467495",
        "Data": [
            {
                "TypeKey": "1310708577",
                "TypeValue": [
                    {
                        "DetailData": 20,
                        "MetricName": "l7Flow_singleIpRequest"
                    }
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

