**Example 1: 查询特定 HTTP 协议版本下的 Top URL Path 流量数据**

查询特定 HTTP 协议版本（HTTP/1.0、HTTP/1.1）下的 Top URL Path 流量数据。

Input: 

```
tccli teo DescribeTopL7AnalysisData --cli-unfold-argument  \
    --Area mainland \
    --Interval day \
    --Limit 1 \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --MetricName l7Flow_outFlux_url \
    --Filters.0.Key protocol \
    --Filters.0.Operator equals \
    --Filters.0.Value HTTP/1.0 HTTP/1.1 \
    --ZoneIds zone-2mzegj4vln5f
```

Output: 
```
{
    "Response": {
        "RequestId": "7c499897-8ad9-4a2d-884e-6154f283d723",
        "Data": [
            {
                "DetailData": [
                    {
                        "Key": "path",
                        "Value": 1210001
                    }
                ],
                "TypeKey": "251227260"
            }
        ],
        "TotalCount": 1
    }
}
```

