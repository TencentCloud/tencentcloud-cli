**Example 1: 查询可用区信息（可用区中文名称）**



Input: 

```
tccli api DescribeZones --cli-unfold-argument  \
    --Product xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 5,
        "ZoneSet": [
            {
                "ZoneState": "UNAVAILABLE",
                "ZoneId": "100001",
                "Zone": "ap-guangzhou-1",
                "ZoneName": "广州一区"
            },
            {
                "ZoneState": "AVAILABLE",
                "ZoneId": "100002",
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区"
            },
            {
                "ZoneState": "AVAILABLE",
                "ZoneId": "100003",
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区"
            },
            {
                "ZoneState": "AVAILABLE",
                "ZoneId": "100004",
                "Zone": "ap-guangzhou-4",
                "ZoneName": "广州四区"
            },
            {
                "ZoneState": "AVAILABLE",
                "ZoneId": "100005",
                "Zone": "ap-guangzhou-5",
                "ZoneName": "广州五区"
            }
        ],
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

