**Example 1: 查询指定域名下的 Top 函数名称请求数数据**



Input: 

```
tccli teo DescribeTopFunctionAnalysisData --cli-unfold-argument  \
    --ZoneIds zone-2mzegj4vln5f \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --MetricName function_requestCount_functionName \
    --Area mainland \
    --Interval day \
    --Limit 1 \
    --Filters.0.Key domain \
    --Filters.0.Operator equals \
    --Filters.0.Value www.baidu.com
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
                        "Key": "test051301-zone-2mzegj4vln5f-13000000",
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

