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
                "Zone": "ap-guangzhou-1",
                "ZoneId": 0,
                "ZoneState": 0,
                "RegionId": 0,
                "ZoneName": "广州一区",
                "ZoneResourceState": 0
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

