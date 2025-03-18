**Example 1: 查询集群信息**

查询集群信息

Input: 

```
tccli cdwpg DescribeInstanceInfo --cli-unfold-argument  \
    --InstanceId cdwpg-4dwmcu5n
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "94e9f7c9-8431-45b4-9167-1d2a648d3d07",
        "SimpleInstanceInfo": {
            "AccessInfo": "192.168.22.104:9000",
            "ChargeProperties": {
                "ChargeType": "POSTPAID_BY_HOUR",
                "RenewFlag": 0,
                "TimeSpan": 1,
                "TimeUnit": "h"
            },
            "CreateTime": "2025-03-03 14:25:01",
            "ExpireTime": "0000.00.00 00:00:00",
            "ID": 595,
            "InstanceId": "cdwpg-4dwmcu5n",
            "InstanceName": "cdwpg_test100",
            "Region": "eu-frankfurt",
            "RenewFlag": 0,
            "Resources": [
                {
                    "Count": 2,
                    "DiskSpec": {
                        "DiskCount": 10,
                        "DiskSize": 20,
                        "DiskType": "CLOUD_HSSD"
                    },
                    "SpecName": "S_4_16_H_CN",
                    "Type": "cn"
                },
                {
                    "Count": 2,
                    "DiskSpec": {
                        "DiskCount": 10,
                        "DiskSize": 20,
                        "DiskType": "CLOUD_HSSD"
                    },
                    "SpecName": "S_4_16_H",
                    "Type": "dn"
                }
            ],
            "Status": 2,
            "Tags": [],
            "UserSubnetID": "subnet-d05spb5o",
            "UserVPCID": "vpc-5wsen2rn",
            "Version": "3.16.9.3",
            "Zone": "eu-frankfurt-1"
        }
    }
}
```

