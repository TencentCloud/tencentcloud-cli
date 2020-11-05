**Example 1: Querying the Chinese name of an availability zone**

This example shows you how to query information of availability zones in the Guangzhou region. To return its Chinese name of the availability zone, you need to pass the parameter `Language=zh-CN`.

Input: 

```
tccli cvm DescribeZones --cli-unfold-argument  \
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
            }
        ],
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

**Example 2: Querying the English name of an availability zone**

This example shows you how to query the availability zones in the Guangzhou region. Its English name will be returned by default if the parameter `Language` is not passed in.

Input: 

```
tccli cvm DescribeZones --cli-unfold-argument ```

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
            }
        ],
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

