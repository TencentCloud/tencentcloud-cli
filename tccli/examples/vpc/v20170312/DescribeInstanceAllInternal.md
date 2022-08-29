**Example 1: 获取Instance相关的VPC信息**



Input: 

```
tccli vpc DescribeInstanceAllInternal --cli-unfold-argument  \
    --InstanceId ins-asdasdd
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
                        "AttachType": 0,
                        "VpcId": 16769060,
                        "EniId": 2609655,
                        "Description": "",
                        "Business": "",
                        "TrunkingFlag": 0,
                        "SubnetId": 2018313,
                        "Mac": "52:54:00:51:48:6B",
                        "UniqueSubnetId": "subnet-oiqmspv4",
                        "Owner": "251197522",
                        "TagProto": "vlan",
                        "CreateTime": "2021-06-17 11:24:24",
                        "Name": "ins-yn79rou1 Primary ENI",
                        "IfnIndex": 0,
                        "UniqueEniId": "eni-nl6govs9",
                        "AttachTime": "2021-06-17 11:24:24",
                        "BFlushSubEniHavip": 0,
                        "UniqueVpcId": "vpc-7zayowkt",
                        "State": 1,
                        "ArpLearningFlag": 1,
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
                        "ElasticNetworkCardName": "veth_51486Bf0",
                        "BusinessOwner": "",
                        "BridgeName": "vbr16769060",
                        "Type": 1
                    },
                    {
                        "AttachType": 0,
                        "VpcId": 80216,
                        "EniId": 3825148,
                        "Description": "",
                        "Business": "TKE",
                        "TrunkingFlag": 0,
                        "SubnetId": 1873271,
                        "Mac": "20:90:6F:6A:9D:4A",
                        "UniqueSubnetId": "subnet-l82vfhw4",
                        "Owner": "251010724_skip",
                        "TagProto": "",
                        "CreateTime": "2022-03-25 16:46:21",
                        "Name": "12345",
                        "IfnIndex": 0,
                        "UniqueEniId": "eni-bmsu454f",
                        "AttachTime": "2022-03-25 16:46:22",
                        "BFlushSubEniHavip": 0,
                        "UniqueVpcId": "vpc-q2nxods9",
                        "State": 1,
                        "ArpLearningFlag": 1,
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
                        "ElasticNetworkCardName": "veni_vFspoqZc",
                        "BusinessOwner": "TKE",
                        "BridgeName": "vbr80216",
                        "Type": 0
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
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

