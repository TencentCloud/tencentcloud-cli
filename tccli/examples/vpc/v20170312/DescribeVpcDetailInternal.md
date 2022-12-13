**Example 1: demo**



Input: 

```
tccli vpc DescribeVpcDetailInternal --cli-unfold-argument  \
    --Owner 251197522 \
    --UniqueVpcId vpc-7zayowkt
```

Output: 
```
{
    "Response": {
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
        "VbcRoutePublishType": 0,
        "Count": 0,
        "CdcType": 0,
        "BypassPVGWSticky": 0,
        "Max": 167837695,
        "DirectSend": 0,
        "NextGenFlag": 0,
        "HBFlag": 0,
        "GatewayIp": "0.0.0.0",
        "CreateTime": "2021-05-10 15:40:11",
        "VisibleFlag": 1,
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
                        "UniqueVpcId": "vpc-7zayowkt",
                        "CdcFlag": 0,
                        "Subnet": "10.4.0.0",
                        "Mask": "255.255.192.0",
                        "BroadcastFlag": 0,
                        "UniqueCdcId": "",
                        "IntMask": 18,
                        "SyncAclToTgwFlag": 0,
                        "ZoneId": 100001,
                        "Owner": "251197522",
                        "UniqueSubnetId": "subnet-cx7wjby6",
                        "LocalZoneFlag": 0,
                        "SubnetId": 2009875,
                        "RemoteVpcSnatFlag": 0,
                        "Type": 0,
                        "Name": "aaa"
                    },
                    {
                        "DefaultFlag": 0,
                        "VpcId": 16769060,
                        "UniqueVpcId": "vpc-7zayowkt",
                        "CdcFlag": 0,
                        "Subnet": "10.4.128.0",
                        "Mask": "255.255.128.0",
                        "BroadcastFlag": 0,
                        "UniqueCdcId": "",
                        "IntMask": 17,
                        "SyncAclToTgwFlag": 0,
                        "ZoneId": 100002,
                        "Owner": "251197522",
                        "UniqueSubnetId": "subnet-oiqmspv4",
                        "LocalZoneFlag": 0,
                        "SubnetId": 2018313,
                        "RemoteVpcSnatFlag": 0,
                        "Type": 0,
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
        "CloudMonitorFlag": 0,
        "Router": [
            {
                "RouterId": 201975,
                "Name": "default",
                "UniqueRouterId": "router-8uuhixa2"
            }
        ],
        "RequestId": "5bba9ec3-58c4-462b-8284-44fdfb923492"
    }
}
```

