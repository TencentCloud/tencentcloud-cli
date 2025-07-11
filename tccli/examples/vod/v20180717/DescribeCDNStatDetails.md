**Example 1: 查询域名 example.com 中国大陆的流量数据。**

查询域名 example.com 中国大陆的流量数据。

Input: 

```
tccli vod DescribeCDNStatDetails --cli-unfold-argument  \
    --DomainNames example.com \
    --StartTime 2018-12-01T00:00:00+08:00 \
    --EndTime 2018-12-03T00:00:00+08:00 \
    --Area 'Chinese Mainland' \
    --Metric Traffic
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

