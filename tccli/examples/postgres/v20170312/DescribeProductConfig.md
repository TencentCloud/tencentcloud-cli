**Example 1: 查询某个地域某个可用区的售卖规格信息**



Input: 

```
tccli postgres DescribeProductConfig --cli-unfold-argument  \
    --Zone ap-guangzhou-2
```

Output: 
```
{
    "Response": {
        "RequestId": "eaa0a364-08c9-42f6-888e-4e3b7e99b50d",
        "SpecInfoList": [
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-2",
                "SpecItemInfoList": [
                    {
                        "SpecCode": "cdb.pg.z1.2g",
                        "Version": "9.5.4",
                        "VersionName": "PostgreSQL 9.5.4",
                        "Cpu": 1,
                        "Memory": 2048,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 2100,
                        "Pid": 11004,
                        "Type": "TS85"
                    }
                ]
            }
        ]
    }
}
```

