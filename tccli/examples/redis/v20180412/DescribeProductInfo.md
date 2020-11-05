**Example 1: Request Sample**



Input: 

```
tccli redis DescribeProductInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "RegionId": "ap-guangzhou",
                "RegionName": "Guangzhou",
                "RegionShortName": "GZ",
                "Area": "South China",
                "ZoneSet": [
                    {
                        "ZoneId": "ap-guangzhou-2",
                        "ZoneName": "Guangzhou Zone 2",
                        "IsSaleout": false,
                        "IsDefault": false,
                        "NetWorkType": [
                            "basenet",
                            "vpcnet"
                        ],
                        "ProductSet": [
                            {
                                "Type": 7,
                                "TypeName": "Redis cluster edition",
                                "MinBuyNum": 1,
                                "MaxBuyNum": 10,
                                "Saleout": false,
                                "Engine": "Redis community edition",
                                "Version": "Redis 4.0",
                                "TotalSize": [
                                    "12",
                                    "20",
                                    "32",
                                    "64",
                                    "96",
                                    "128",
                                    "256",
                                    "384",
                                    "512",
                                    "768",
                                    "1024",
                                    "2048",
                                    "3072",
                                    "4096"
                                ],
                                "ShardSize": [
                                    "4",
                                    "8",
                                    "12",
                                    "16",
                                    "20",
                                    "24",
                                    "32"
                                ],
                                "ReplicaNum": [
                                    "1",
                                    "2",
                                    "3",
                                    "4",
                                    "5"
                                ],
                                "ShardNum": [
                                    "3",
                                    "5",
                                    "8",
                                    "12",
                                    "16",
                                    "24",
                                    "32",
                                    "40",
                                    "48",
                                    "64",
                                    "80",
                                    "96",
                                    "128"
                                ],
                                "PayMode": "1",
                                "EnableRepicaReadOnly": true
                            },
                            {
                                "Type": 4,
                                "TypeName": "CKV cluster edition",
                                "MinBuyNum": 1,
                                "MaxBuyNum": 10,
                                "Saleout": false,
                                "Engine": "Tencent Cloud CKV",
                                "Version": "Redis 3.2",
                                "TotalSize": [
                                    "12",
                                    "20",
                                    "32",
                                    "64",
                                    "96",
                                    "128",
                                    "256",
                                    "384",
                                    "512",
                                    "768",
                                    "1024",
                                    "2048",
                                    "3072",
                                    "4096"
                                ],
                                "ShardSize": [
                                    "4",
                                    "8",
                                    "16",
                                    "24",
                                    "32",
                                    "48",
                                    "64",
                                    "80",
                                    "96",
                                    "128",
                                    "160",
                                    "192",
                                    "256",
                                    "320",
                                    "384"
                                ],
                                "ReplicaNum": [
                                    "1",
                                    "2",
                                    "3",
                                    "4",
                                    "5"
                                ],
                                "ShardNum": [
                                    "3",
                                    "5",
                                    "8",
                                    "12",
                                    "16",
                                    "24",
                                    "32",
                                    "40",
                                    "48",
                                    "64",
                                    "80",
                                    "96",
                                    "128"
                                ],
                                "PayMode": "1",
                                "EnableRepicaReadOnly": false
                            },
                            {
                                "Type": 2,
                                "TypeName": "Redis master/slave edition",
                                "MinBuyNum": 1,
                                "MaxBuyNum": 10,
                                "Saleout": false,
                                "Engine": "Redis community edition",
                                "Version": "Redis 2.8",
                                "TotalSize": [
                                    "1",
                                    "2",
                                    "4",
                                    "8",
                                    "12",
                                    "16",
                                    "20",
                                    "24",
                                    "32",
                                    "40",
                                    "48",
                                    "60",
                                    "0.25"
                                ],
                                "ShardSize": [
                                    "1",
                                    "2",
                                    "4",
                                    "8",
                                    "12",
                                    "16",
                                    "20",
                                    "24",
                                    "32",
                                    "40",
                                    "48",
                                    "60",
                                    "0.25"
                                ],
                                "ReplicaNum": [
                                    "1"
                                ],
                                "ShardNum": [
                                    "1"
                                ],
                                "PayMode": "1",
                                "EnableRepicaReadOnly": false
                            },
                            {
                                "Type": 5,
                                "TypeName": "Redis standalone edition",
                                "MinBuyNum": 1,
                                "MaxBuyNum": 10,
                                "Saleout": false,
                                "Engine": "Redis community edition",
                                "Version": "Redis 2.8",
                                "TotalSize": [
                                    "1",
                                    "2",
                                    "4",
                                    "8",
                                    "12",
                                    "16",
                                    "20",
                                    "24",
                                    "32",
                                    "40",
                                    "48",
                                    "60"
                                ],
                                "ShardSize": [
                                    "1",
                                    "2",
                                    "4",
                                    "8",
                                    "12",
                                    "16",
                                    "20",
                                    "24",
                                    "32",
                                    "40",
                                    "48",
                                    "60"
                                ],
                                "ReplicaNum": [
                                    "0"
                                ],
                                "ShardNum": [
                                    "1"
                                ],
                                "PayMode": "1",
                                "EnableRepicaReadOnly": false
                            },
                            {
                                "Type": 2,
                                "TypeName": "Redis master-slave edition",
                                "MinBuyNum": 1,
                                "MaxBuyNum": 10,
                                "Saleout": false,
                                "Engine": "Redis community edition",
                                "Version": "Redis 2.8",
                                "TotalSize": [
                                    "1",
                                    "2",
                                    "4",
                                    "8",
                                    "12",
                                    "16",
                                    "20",
                                    "24",
                                    "32",
                                    "40",
                                    "48",
                                    "60"
                                ],
                                "ShardSize": [
                                    "1",
                                    "2",
                                    "4",
                                    "8",
                                    "12",
                                    "16",
                                    "20",
                                    "24",
                                    "32",
                                    "40",
                                    "48",
                                    "60"
                                ],
                                "ReplicaNum": [
                                    "1"
                                ],
                                "ShardNum": [
                                    "1"
                                ],
                                "PayMode": "0",
                                "EnableRepicaReadOnly": false
                            },
                            {
                                "Type": 3,
                                "TypeName": "CKV standalone edition",
                                "MinBuyNum": 1,
                                "MaxBuyNum": 10,
                                "Saleout": false,
                                "Engine": "Tencent Cloud CKV",
                                "Version": "Redis 3.2",
                                "TotalSize": [
                                    "4",
                                    "8",
                                    "16",
                                    "24",
                                    "32",
                                    "48",
                                    "64",
                                    "80",
                                    "96",
                                    "128",
                                    "160",
                                    "192",
                                    "256",
                                    "320",
                                    "384"
                                ],
                                "ShardSize": [
                                    "4",
                                    "8",
                                    "16",
                                    "24",
                                    "32",
                                    "48",
                                    "64",
                                    "80",
                                    "96",
                                    "128",
                                    "160",
                                    "192",
                                    "256",
                                    "320",
                                    "384"
                                ],
                                "ReplicaNum": [
                                    "0"
                                ],
                                "ShardNum": [
                                    "1"
                                ],
                                "PayMode": "1",
                                "EnableRepicaReadOnly": false
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "3c5730c6-02f2-46fd-8bf1-725b8b608fb9"
    }
}
```

