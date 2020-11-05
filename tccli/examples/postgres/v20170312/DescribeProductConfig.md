**Example 1: Querying purchasable specification information in a specified AZ of a specified region**



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
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.2g",
                        "Version": "9.3.5",
                        "VersionName": "PostgreSQL 9.3.5",
                        "Cpu": 1,
                        "Memory": 2048,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 2100,
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.4g",
                        "Version": "9.5.4",
                        "VersionName": "PostgreSQL 9.5.4",
                        "Cpu": 2,
                        "Memory": 4096,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 4000,
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.4g",
                        "Version": "9.3.5",
                        "VersionName": "PostgreSQL 9.3.5",
                        "Cpu": 2,
                        "Memory": 4096,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 4000,
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.8g",
                        "Version": "9.3.5",
                        "VersionName": "PostgreSQL 9.3.5",
                        "Cpu": 4,
                        "Memory": 8192,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 6500,
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.8g",
                        "Version": "9.5.4",
                        "VersionName": "PostgreSQL 9.5.4",
                        "Cpu": 4,
                        "Memory": 8192,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 6500,
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.16g",
                        "Version": "9.3.5",
                        "VersionName": "PostgreSQL 9.3.5",
                        "Cpu": 8,
                        "Memory": 16384,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 16800,
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.16g",
                        "Version": "9.5.4",
                        "VersionName": "PostgreSQL 9.5.4",
                        "Cpu": 8,
                        "Memory": 16384,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 16800,
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.32g",
                        "Version": "9.3.5",
                        "VersionName": "PostgreSQL 9.3.5",
                        "Cpu": 16,
                        "Memory": 32768,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 23000,
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.32g",
                        "Version": "9.5.4",
                        "VersionName": "PostgreSQL 9.5.4",
                        "Cpu": 16,
                        "Memory": 32768,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 23000,
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.48g",
                        "Version": "9.5.4",
                        "VersionName": "PostgreSQL 9.5.4",
                        "Cpu": 22,
                        "Memory": 49152,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 36300,
                        "pid": 11004
                    },
                    {
                        "SpecCode": "cdb.pg.z1.48g",
                        "Version": "9.3.5",
                        "VersionName": "PostgreSQL 9.3.5",
                        "Cpu": 22,
                        "Memory": 49152,
                        "MaxStorage": 1000,
                        "MinStorage": 10,
                        "Qps": 36300,
                        "pid": 11004
                    }
                ]
            }
        ]
    }
}
```

