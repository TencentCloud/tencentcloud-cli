**Example 1: demo**



Input: 

```
tccli vpc DescribeVpcInner --cli-unfold-argument  \
    --Owner 251197522 \
    --UniqueVpcId vpc-7zayowkt
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "VpcDetailSet": [
            {
                "DefaultFlag": 0,
                "VpcId": 16769060,
                "TransChannelFlag": 0,
                "UniqueVpcId": "vpc-7zayowkt",
                "DSCPFlag": 0,
                "Mask": "255.255.0.0",
                "RegionId": 0,
                "SubnetRoutePriority": 0,
                "Owner": "251197522",
                "Id": 495906,
                "Subnet": "10.0.0.0",
                "Min": 167772160,
                "OwnedFlag": 0,
                "VbcDcFlag": 0,
                "OwnerLevel": -1,
                "IntMask": 16,
                "DhcpFlag": 1,
                "Type": 0,
                "MulticastFlag": 0,
                "CdcType": 0,
                "BypassPVGWSticky": 0,
                "Max": 167837695,
                "DirectSend": 0,
                "NextGenFlag": 0,
                "HBFlag": 0,
                "GatewayIp": "0.0.0.0",
                "CreateTime": "2021-05-10 15:40:11",
                "Count": 0,
                "AssistCidrs": [
                    {
                        "Subnet": "10.1.0.0",
                        "SubnetUseInfo": [],
                        "Mask": "255.255.0.0",
                        "IntMask": 16,
                        "AssistType": 1
                    },
                    {
                        "Subnet": "10.4.0.0",
                        "SubnetUseInfo": [
                            {
                                "DefaultFlag": 0,
                                "VpcId": 16769060,
                                "CdcFlag": 0,
                                "UniqueVpcId": "vpc-7zayowkt",
                                "Subnet": "10.4.0.0",
                                "BroadcastFlag": 0,
                                "UniqueCdcId": "",
                                "Mask": "255.255.192.0",
                                "ZoneId": 100001,
                                "Owner": "251197522",
                                "UniqueSubnetId": "subnet-cx7wjby6",
                                "IntMask": 18,
                                "SubnetId": 2009875,
                                "LocalZoneFlag": 0,
                                "Type": 0,
                                "RemoteVpcSnatFlag": 0,
                                "Name": "aaa"
                            },
                            {
                                "DefaultFlag": 0,
                                "VpcId": 16769060,
                                "CdcFlag": 0,
                                "UniqueVpcId": "vpc-7zayowkt",
                                "Subnet": "10.4.128.0",
                                "BroadcastFlag": 0,
                                "UniqueCdcId": "",
                                "Mask": "255.255.128.0",
                                "ZoneId": 100002,
                                "Owner": "251197522",
                                "UniqueSubnetId": "subnet-oiqmspv4",
                                "IntMask": 17,
                                "SubnetId": 2018313,
                                "LocalZoneFlag": 0,
                                "Type": 0,
                                "RemoteVpcSnatFlag": 0,
                                "Name": "testtt"
                            }
                        ],
                        "Mask": "255.255.0.0",
                        "IntMask": 16,
                        "AssistType": 0
                    },
                    {
                        "Subnet": "10.5.0.0",
                        "SubnetUseInfo": [],
                        "Mask": "255.255.0.0",
                        "IntMask": 16,
                        "AssistType": 0
                    },
                    {
                        "Subnet": "10.6.0.0",
                        "SubnetUseInfo": [],
                        "Mask": "255.255.0.0",
                        "IntMask": 16,
                        "AssistType": 0
                    }
                ],
                "Name": "cissytest",
                "BraceLinkFlag": 0,
                "Region": "",
                "LearnTsvIp": 1,
                "CloudMonitorFlag": 0
            }
        ],
        "RequestId": "27d39428-5dc1-41af-9a5c-8bd376709301"
    }
}
```

