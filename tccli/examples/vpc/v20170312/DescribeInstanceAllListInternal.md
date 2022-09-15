**Example 1: demo**



Input: 

```
tccli vpc DescribeInstanceAllListInternal --cli-unfold-argument  \
    --InstanceId ins-yn79rou1
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "WanInLimit": 0,
                "LanInLimit": 1610612736,
                "UniqueCdcId": "",
                "Uuid": "84f9a2ad-6659-4864-808c-bd17f3c2acea",
                "CdcFlag": 0,
                "LanOutLimit": 1610612736,
                "InstanceId": "ins-yn79rou1",
                "Eni": [
                    {
                        "VpcId": 16769060,
                        "EniId": 2609655,
                        "UniqueVpcId": "vpc-7zayowkt",
                        "TrunkingFlag": 0,
                        "SubnetId": 2018313,
                        "PrivateIpSet": [
                            {
                                "Description": "",
                                "State": 1,
                                "DhcpIpFlag": 0,
                                "WanIp": "0.0.0.0",
                                "HavIpFlag": 0,
                                "PrivateIp": "10.4.128.5",
                                "Type": 1,
                                "CreateTime": "2021-06-17 11:24:24",
                                "BlockedFlag": 0
                            }
                        ],
                        "EniQos": {
                            "RdmaFlag": 0,
                            "PortMax": 65535,
                            "DirectSend": 0,
                            "NSHType": 0,
                            "PortMin": 1025,
                            "DiffAzStatsFlag": 1,
                            "QosType": 0,
                            "DetailDiffAzStatsFlag": 0,
                            "QosQualityLevel": 26
                        },
                        "Owner": "251197522",
                        "AttachType": 0,
                        "UniqueEniId": "eni-nl6govs9",
                        "FlushSubEniHavipFlag": 0,
                        "State": 1,
                        "ArpLearningFlag": 1,
                        "BusinessOwner": "",
                        "BridgeName": "vbr16769060",
                        "Type": 1,
                        "IfnIndex": 0,
                        "Description": "",
                        "Business": "",
                        "Mac": "52:54:00:51:48:6B",
                        "TagProto": "vlan",
                        "CreateTime": "2021-06-17 11:24:24",
                        "Name": "ins-yn79rou1 Primary ENI",
                        "AttachTime": "2021-06-17 11:24:24",
                        "UniqueSubnetId": "subnet-oiqmspv4",
                        "ElasticNetworkCardName": "veth_51486Bf0"
                    },
                    {
                        "VpcId": 80216,
                        "EniId": 3825148,
                        "UniqueVpcId": "vpc-q2nxods9",
                        "TrunkingFlag": 0,
                        "SubnetId": 1873271,
                        "PrivateIpSet": [
                            {
                                "Description": "",
                                "State": 1,
                                "DhcpIpFlag": 0,
                                "WanIp": "0.0.0.0",
                                "HavIpFlag": 0,
                                "PrivateIp": "10.0.1.2",
                                "Type": 0,
                                "CreateTime": "2022-03-25 16:46:21",
                                "BlockedFlag": 0
                            },
                            {
                                "Description": "",
                                "State": 1,
                                "DhcpIpFlag": 0,
                                "WanIp": "0.0.0.0",
                                "HavIpFlag": 0,
                                "PrivateIp": "10.0.1.4",
                                "Type": 1,
                                "CreateTime": "2022-03-25 16:46:21",
                                "BlockedFlag": 0
                            }
                        ],
                        "EniQos": {
                            "RdmaFlag": 0,
                            "PortMax": 65535,
                            "DirectSend": 0,
                            "NSHType": 0,
                            "PortMin": 1025,
                            "DiffAzStatsFlag": 1,
                            "QosType": 0,
                            "DetailDiffAzStatsFlag": 0,
                            "QosQualityLevel": 26
                        },
                        "Owner": "251010724_skip",
                        "AttachType": 0,
                        "UniqueEniId": "eni-bmsu454f",
                        "FlushSubEniHavipFlag": 0,
                        "State": 1,
                        "ArpLearningFlag": 1,
                        "BusinessOwner": "TKE",
                        "BridgeName": "vbr80216",
                        "Type": 0,
                        "IfnIndex": 0,
                        "Description": "",
                        "Business": "TKE",
                        "Mac": "20:90:6F:6A:9D:4A",
                        "TagProto": "",
                        "CreateTime": "2022-03-25 16:46:21",
                        "Name": "12345",
                        "AttachTime": "2022-03-25 16:46:22",
                        "UniqueSubnetId": "subnet-l82vfhw4",
                        "ElasticNetworkCardName": "veni_vFspoqZc"
                    }
                ],
                "InstanceFamily": "",
                "Owner": "251197522",
                "HostType": "",
                "VMem": 0,
                "Bandwidth": 1,
                "HostIp": "100.99.164.201",
                "WanOutLimit": 1048576,
                "SnHypervisor": "",
                "VCpu": 0,
                "CreateTime": "2021-06-17 11:24:24"
            }
        ],
        "RequestId": "7986da7d-a967-4d6b-9950-4c8a75f4a0ba"
    }
}
```

