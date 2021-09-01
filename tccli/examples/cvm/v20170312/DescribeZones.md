**Example 1: 查询可用区信息（可用区中文名称）**

查询广州地域的可用区信息。返回可用区的中文名称需要传参Language=zh-CN。

Input: 

```
tccli cvm DescribeZones --cli-unfold-argument ```

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

**Example 2: 查询可用区信息（可用区英文名称）**

查询广州地域的可用区信息。不传Language参数默认返回可用区的英文名称。

Input: 

```
tccli cvm DescribeZones --cli-unfold-argument ```

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
                "ZoneName": "Guangzhou Zone 1"
            },
            {
                "ZoneState": "AVAILABLE",
                "ZoneId": "100002",
                "Zone": "ap-guangzhou-2",
                "ZoneName": "Guangzhou Zone 2"
            },
            {
                "ZoneState": "AVAILABLE",
                "ZoneId": "100003",
                "Zone": "ap-guangzhou-3",
                "ZoneName": "Guangzhou Zone 3"
            },
            {
                "ZoneState": "AVAILABLE",
                "ZoneId": "100004",
                "Zone": "ap-guangzhou-4",
                "ZoneName": "Guangzhou Zone 4"
            },
            {
                "ZoneState": "AVAILABLE",
                "ZoneId": "100005",
                "Zone": "ap-guangzhou-5",
                "ZoneName": "Guangzhou Zone 5"
            }
        ],
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

