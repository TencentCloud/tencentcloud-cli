**Example 1: This example shows you how to query bandwidth statistics of the `123.vod2.myqcloud.com` and `test.a.com` domain names with 5-minute granularity between December 1, 2018 to December 7, 2018.**

This example shows you how to query the CDN traffic statistics between December 1, 2018 (inclusive) and December 3, 2018 (inclusive).

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

**Example 2: Querying CDN traffic statistics of VOD**

This example shows you how to query the CDN traffic statistics between December 1, 2018 (inclusive) and December 3, 2018 (inclusive).

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

**Example 3: Querying bandwidth statistics of all domain names between December 1, 2018 and December 7, 2018 by an admin**



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

