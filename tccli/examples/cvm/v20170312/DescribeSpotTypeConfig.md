**Example 1: 查询用户可购买的竞价机型信息列表**

查询用户可购买的竞价机型信息列表

Input: 

```
tccli cvm DescribeSpotTypeConfig --cli-unfold-argument  \
    --instanceTypeList S1.SMALL1
```

Output: 
```
{
    "Response": {
        "SpotTypeConfigSet": [
            {
                "gid": 6,
                "zone": "ap-guangzhou-2",
                "zone_id": 100002,
                "instance_type": "S1.SMALL1",
                "instance_family": "S1",
                "cpu": 1,
                "mem": 1,
                "quota": 100,
                "capacity_allot": 6,
                "price_cur": 0.11,
                "cvmQuota": 94
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

**Example 2: 查询可用区信息（可用区中文名称）**

查询广州地域的可用区信息。返回可用区的中文名称需要传参Language=zh-CN。

Input: 

```
tccli cvm DescribeSpotTypeConfig --cli-unfold-argument  \
    --Language zh-CN
```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
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
            }
        ],
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

