**Example 1: 查询所有可用区**



Input: 

```
tccli sqlserver DescribeZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "c877d7ce-bde9-48dc-bf8c-9efb01570caa",
        "TotalCount": 34,
        "ZoneSet": [
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 1,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 5,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 17,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 16,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 14,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 6,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 2,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 14,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 3,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 14,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 4,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 26,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 20,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 13,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 5,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 23,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 3,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 4,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 6,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 5,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 1,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 4,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 13,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 6,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 21,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 25,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 24,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 13,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 19,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 3,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 2,
                "Version": "2008R2"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 22,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "SpecId": 2,
                "Version": "2012SP3"
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "SpecId": 18,
                "Version": "2012SP3"
            }
        ]
    }
}
```

