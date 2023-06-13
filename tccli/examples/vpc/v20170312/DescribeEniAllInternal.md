**Example 1: 用于获取弹性网卡极其附属的信息**

用于获取弹性网卡极其附属的信息。

Input: 

```
tccli vpc DescribeEniAllInternal --cli-unfold-argument  \
    --Uuid xxx \
    --SafeGroupId xxx \
    --State 0 \
    --IfnName xxx \
    --Type 0 \
    --UniqueSubnetId xxx \
    --VpcId 123 \
    --EniId 1 \
    --Description xxx \
    --Business xxx \
    --InstanceId xxx \
    --Mac xxx \
    --Offset 0 \
    --SubnetId 123 \
    --Name xxx \
    --TagValue xxx \
    --Limit 100 \
    --BusinessOwner xxx \
    --TagKey xxx \
    --EniPrivateIp 1.1.1.1 \
    --UniqueEniId xxx \
    --Owner 251198225
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "EniSet": [
            {
                "DefaultFlag": 0,
                "VpcId": 16769060,
                "EniId": 2609655,
                "UniqueVpcId": "vpc-7zayowkt",
                "Mask": "255.255.128.0",
                "VpcDefaultFlag": 0,
                "TrunkingFlag": 0,
                "SubnetId": 2018313,
                "PrivateIpSet": [
                    {
                        "Description": "xxx",
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
                    "PortMax": 65535,
                    "DirectSend": 0,
                    "PortMin": 1025,
                    "QosType": 0
                },
                "AclId": 95805,
                "Owner": "251197522",
                "UniqAclId": "acl-r762el0i",
                "UniqueCdcId": "xxx",
                "Subnet": "10.4.128.0",
                "UniqueEniId": "eni-nl6govs9",
                "VpcIntMask": 16,
                "VpcMask": "255.255.0.0",
                "ZoneId": 100002,
                "Instance": {
                    "WanInLimit": 0,
                    "IfnIndex": 0,
                    "LanInLimit": 1610612736,
                    "AttachType": 0,
                    "AttachTime": "2021-06-17 11:24:24",
                    "LanOutLimit": 1610612736,
                    "InstanceId": "ins-yn79rou1",
                    "UniqueCdcId": "xxx",
                    "Bandwidth": 1,
                    "Owner": "251197522",
                    "CdcFlag": 0,
                    "HostIp": "100.99.164.201",
                    "WanOutLimit": 1048576,
                    "BridgeName": "vbr16769060",
                    "Uuid": "84f9a2ad-6659-4864-808c-bd17f3c2acea"
                },
                "State": 1,
                "ArpLearningFlag": 1,
                "Ipv6": [
                    {
                        "Description": "",
                        "State": 1,
                        "WanIp": "",
                        "HavIpFlag": 0,
                        "PrivateIp": "2402:4e00:1000:2b00:0:90fb:c2c4:6995",
                        "Type": 0,
                        "CreateTime": "2020-07-07 16:16:28",
                        "BlockedFlag": 0
                    }
                ],
                "IntMask": 17,
                "BusinessOwner": "xxx",
                "DhcpFlag": 0,
                "Type": 1,
                "Description": "xx",
                "Business": "xx",
                "VpcSubnet": "10.0.0.0",
                "CdcFlag": 0,
                "Mac": "52:54:00:51:48:6B",
                "TagProto": "vlan",
                "CreateTime": "2021-06-17 11:24:24",
                "StreamFlowNumber": 1,
                "Name": "ins-yn79rou1 Primary ENI",
                "StreamFlow": [
                    {
                        "Name": "tsss",
                        "Uin": "100000072292",
                        "LogId": "38ed2b0e-28ac-47d3-834f-b425d6f83a78",
                        "Policy": 1,
                        "LogState": 0,
                        "Description": "xxx"
                    }
                ],
                "AclName": "ttttt",
                "LocalZoneFlag": 0,
                "VpcName": "cissytest",
                "UniqueSubnetId": "subnet-oiqmspv4",
                "ElasticNetworkCardName": "veth_51486Bf0",
                "SubnetName": "testtt"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

