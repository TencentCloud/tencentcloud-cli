**Example 1: 列出 Prometheus 服务可用区**

列出 Prometheus 服务可用区

Input: 

```
tccli monitor DescribePrometheusZones --cli-unfold-argument  \
    --RegionId 1234
```

Output: 
```
{
    "Response": {
        "ZoneSet": [
            {
                "ZoneState": 1,
                "ZoneName": "xx",
                "RegionId": 0,
                "Zone": "xx",
                "ZoneId": 160001
            }
        ],
        "RequestId": "xx"
    }
}
```

