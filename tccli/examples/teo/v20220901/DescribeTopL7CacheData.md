**Example 1: 查询指定状态码的top流量数据**



Input: 

```
tccli teo DescribeTopL7CacheData --cli-unfold-argument  \
    --Area mainland \
    --Interval day \
    --Limit 5 \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --MetricName l7Cache_outFlux_cacheType \
    --Filters.0.Key statusCode \
    --Filters.0.Operator equals \
    --Filters.0.Value 2XX 3XX \
    --ZoneIds zone-2mzegj4vln5f
```

Output: 
```
{
    "Response": {
        "RequestId": "64463c6f-3296-47fa-b168-2040f841eed1",
        "Data": [
            {
                "DetailData": [
                    {
                        "Key": "hit",
                        "Value": 5810001
                    },
                    {
                        "Key": "miss",
                        "Value": 658
                    }
                ],
                "TypeKey": "251227260"
            }
        ],
        "TotalCount": 1
    }
}
```

