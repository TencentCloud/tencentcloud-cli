**Example 1: 同步获取架构资源详情**

同步获取架构资源详情

Input: 

```
tccli advisor DescribeArchSync --cli-unfold-argument  \
    --ArchId arch-abc \
    --Refresh True
```

Output: 
```
{
    "Response": {
        "RequestId": "bb286fb6-615a-4255-afaa-56b5ad323706",
        "ArchId": "arch-qq2u80vn",
        "ArchName": "新建一个",
        "CreateTime": "2024-03-12 19:21:46",
        "CreateUin": "1000000001",
        "NodeList": [
            {
                "DiagramId": "24149ecf-7ba5-4eb0-b76b-e988e9d013a9",
                "NodeId": 10558,
                "NodeName": "NAT 网关",
                "NodeRegion": "ap-hongkong",
                "ProductType": "NAT",
                "ResourceList": [
                    {
                        "Attributes": [
                            {
                                "Name": "VpcId",
                                "Value": "vpc-xxx"
                            },
                            {
                                "Name": "Zone",
                                "Value": "ap-hongkong-3"
                            },
                            {
                                "Name": "ZoneId",
                                "Value": "300003"
                            },
                            {
                                "Name": "ZoneName",
                                "Value": "香港三区"
                            },
                            {
                                "Name": "NatProductVersion",
                                "Value": "传统型"
                            },
                            {
                                "Name": "InternetMaxBandwidthOut",
                                "Value": "10"
                            },
                            {
                                "Name": "MaxConcurrentConnection",
                                "Value": "1000000"
                            },
                            {
                                "Name": "CreatedTime",
                                "Value": "2023-04-12 18:54:21"
                            }
                        ],
                        "InstanceId": "nat-xxx",
                        "InstanceName": "xxxxx-hk",
                        "Tags": [
                            {
                                "Key": "k1",
                                "Value": "v1"
                            },
                            {
                                "Key": "k2",
                                "Value": "v2"
                            }
                        ]
                    }
                ]
            },
            {
                "DiagramId": "bfc003f0-0f56-4778-8efb-abe7cbbfabc8",
                "NodeId": 10556,
                "NodeName": "专线网关",
                "NodeRegion": "ap-hongkong",
                "ProductType": "DCG",
                "ResourceList": [
                    {
                        "Attributes": [
                            {
                                "Name": "GatewayType",
                                "Value": "标准型"
                            },
                            {
                                "Name": "CreateTime",
                                "Value": "2023-10-27 10:39:12"
                            }
                        ],
                        "InstanceId": "dcg-xxxx",
                        "InstanceName": "test",
                        "Tags": []
                    }
                ]
            }
        ],
        "UpdateTime": "2024-05-31 11:27:29",
        "UpdateUin": "xxx",
        "VersionName": "1.0.0"
    }
}
```

