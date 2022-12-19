**Example 1: demo**



Input: 

```
tccli vpc DescribeSubnetListInternal --cli-unfold-argument  \
    --Owner 251197522 \
    --UniqueVpcId vpc-7zayowkt \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Total": 3,
        "SubnetSet": [
            {
                "DefaultFlag": 0,
                "VpcId": 16769060,
                "CdcFlag": 0,
                "SubnetId": 2007467,
                "UniqueSubnetId": "subnet-1ufvulum",
                "Owner": "251197522",
                "Subnet": "10.0.0.0",
                "UniqueVpcId": "vpc-7zayowkt",
                "Min": 167772160,
                "UniqueCdcId": "",
                "ZoneId": 100001,
                "IntMask": 24,
                "DhcpFlag": 0,
                "Type": 0,
                "Max": 167772415,
                "GatewayIp": "0.0.0.0",
                "CreateTime": "2021-05-10 15:40:12",
                "RemoteVpcSnatFlag": 0,
                "Name": "test",
                "BroadcastFlag": 0,
                "Mask": "255.255.255.0",
                "SyncAclToTgwFlag": 0,
                "LocalZoneFlag": 0
            }
        ],
        "RequestId": "3f8bc2b6-3ae1-4265-89ff-038396edc068"
    }
}
```

