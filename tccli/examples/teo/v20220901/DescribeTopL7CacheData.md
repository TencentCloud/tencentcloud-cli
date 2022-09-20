**Example 1: 查询七层缓存分析类top流量数据**



Input: 

```
tccli teo DescribeTopL7CacheData --cli-unfold-argument  \
    --Area mainland \
    --Interval day \
    --Limit 5 \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --MetricName l7Cache_outFlux_cacheType
```

Output: 
```
{
    "Response": {
        "RequestId": "64463c6f-4c96-47fa-b168-2040f841eed1",
        "Data": [
            {
                "DetailData": [
                    {
                        "Key": "hit",
                        "Value": 7410001
                    },
                    {
                        "Key": "miss",
                        "Value": 803
                    }
                ],
                "TypeKey": "251227260"
            }
        ],
        "TotalCount": 1
    }
}
```

