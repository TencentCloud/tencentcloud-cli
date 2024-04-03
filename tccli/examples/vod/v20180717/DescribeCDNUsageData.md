**Example 1: 查询点播 CDN 的流量数据**

查询2018年12月1日（含）到2018年12月3日（含）的 CDN 流量数据。

Input: 

```
tccli vod DescribeCDNUsageData --cli-unfold-argument  \
    --StartTime 2018-12-01T00:00:00+08:00 \
    --EndTime 2018-12-03T00:00:00+08:00 \
    --DataType Flux
```

Output: 
```
{
    "Response": {
        "DataInterval": 1440,
        "Data": [
            {
                "Time": "2018-12-01T00:00:00+08:00",
                "Value": 1000000
            },
            {
                "Time": "2018-12-02T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-03T00:00:00+08:00",
                "Value": 1500000
            }
        ],
        "RequestId": "requestId"
    }
}
```

**Example 2: 管理员查询所有域名从2018-12-01到2018-12-07的带宽数据**



Input: 

```
tccli vod DescribeCDNUsageData --cli-unfold-argument  \
    --StartTime 2018-12-01T00:00:00+08:00 \
    --EndTime 2018-12-03T00:00:00+08:00 \
    --DataType Bandwidth \
    --SubAppId 1
```

Output: 
```
{
    "Response": {
        "DataInterval": 1440,
        "Data": [
            {
                "Time": "2018-12-01T00:00:00+08:00",
                "Value": 700000
            },
            {
                "Time": "2018-12-01T05:00:00+08:00",
                "Value": 800000
            },
            {
                "Time": "2018-12-01T10:00:00+08:00",
                "Value": 920000
            }
        ],
        "RequestId": "requestId"
    }
}
```

**Example 3: 查询域名123.vod2.myqcloud.com和test.a.com从2018-12-01到2018-12-07的5分钟粒度的带宽数据**



Input: 

```
tccli vod DescribeCDNUsageData --cli-unfold-argument  \
    --DomainNames 123.vod2.myqcloud.com test.a.com \
    --StartTime 2018-12-01T00:00:00+08:00 \
    --EndTime 2018-12-03T00:00:00+08:00 \
    --DataType Bandwidth \
    --DataInterval 5
```

Output: 
```
{
    "Response": {
        "DataInterval": 5,
        "Data": [
            {
                "Time": "2018-12-01T00:00:00+08:00",
                "Value": 100000
            },
            {
                "Time": "2018-12-01T05:00:00+08:00",
                "Value": 200000
            },
            {
                "Time": "2018-12-01T10:00:00+08:00",
                "Value": 350000
            }
        ],
        "RequestId": "requestId"
    }
}
```

