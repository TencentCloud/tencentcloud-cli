**Example 1: 列出 Prometheus 服务可用区**

列出 Prometheus 服务可用区

Input: 

```
tccli monitor DescribePrometheusZones --cli-unfold-argument  \
    --RegionId 1
```

Output: 
```
{
    "Response": {
        "ZoneSet": [
            {
                "Zone": "abc",
                "ZoneId": 0,
                "ZoneState": 0,
                "RegionId": 0,
                "ZoneName": "abc",
                "ZoneResourceState": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

