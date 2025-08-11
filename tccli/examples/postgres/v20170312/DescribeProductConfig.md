**Example 1: 查询某个地域某个可用区的售卖规格信息**

查询广州三区的售卖规格信息

Input: 

```
tccli postgres DescribeProductConfig --cli-unfold-argument  \
    --Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "RequestId": "eaa0a364-08c9-42f6-888e-4e3b7e99b50d",
        "SpecInfoList": [
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "SupportKMSRegions": [
                    "ap-guangzhou"
                ],
                "SpecItemInfoList": [
                    {
                        "Cpu": 1,
                        "IsSupportTDE": 1,
                        "KernelVersion": "v17.4_r1.7",
                        "MajorVersion": "17",
                        "MaxStorage": 3000,
                        "Memory": 2048,
                        "MinStorage": 10,
                        "Pid": 0,
                        "Qps": 1800,
                        "SpecCode": "pg.it.small2",
                        "Type": "",
                        "Version": "17.4",
                        "VersionName": "PostgreSQL 17"
                    }
                ]
            }
        ]
    }
}
```

