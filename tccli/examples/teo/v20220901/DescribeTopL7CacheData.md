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

**Example 2: 查询缓存命中跟未命中的top流量数据**



Input: 

```
tccli teo DescribeTopL7CacheData --cli-unfold-argument  \
    --Area mainland \
    --Interval day \
    --Limit 5 \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --MetricName l7Cache_outFlux_cacheType \
    --Filters.0.Key cacheType \
    --Filters.0.Operator equals \
    --Filters.0.Value miss hit
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

**Example 3: 查询指定状态码的top流量数据**



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
    --Filters.0.Value 2XX 3XX
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

**Example 4: 根据指定标签的top流量数据**



Input: 

```
tccli teo DescribeTopL7CacheData --cli-unfold-argument  \
    --Area mainland \
    --Interval day \
    --Limit 5 \
    --StartTime 2022-07-31T00:00:00+08:00 \
    --EndTime 2022-08-29T19:17:59+08:00 \
    --MetricName l7Cache_outFlux_cacheType \
    --Filters.0.Key tagKey \
    --Filters.0.Operator equals \
    --Filters.0.Value test1 \
    --Filters.1.Key tagValue \
    --Filters.1.Operator equals \
    --Filters.1.Value a.com b.com
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

