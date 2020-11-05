**Example 1: Querying the Chinese name of an availability zone**

This example shows you how to query information of availability zones in the Guangzhou region. To return its Chinese name of the availability zone, you need to pass the parameter `Language=zh-CN`.

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
                "ZoneName": "Guangzhou Zone 1"
            },
            {
                "ZoneState": "AVAILABLE",
                "ZoneId": "100002",
                "Zone": "ap-guangzhou-2",
                "ZoneName": "Guangzhou Zone 2",
            },
            {
                "ZoneState": "AVAILABLE",
                "ZoneId": "100003",
                "Zone": "ap-guangzhou-3",
                "ZoneName": "Guangzhou Zone 3",
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

**Example 2: Querying the list of spot instance offering**

This example shows you how to query the list of spot instances that are available for purchase.

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

