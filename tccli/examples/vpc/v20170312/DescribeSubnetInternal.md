**Example 1: 用于获取子网信息**



Input: 

```
tccli vpc DescribeSubnetInternal --cli-unfold-argument  \
    --VpcId 123123 \
    --Owner 251198225 \
    --Limit 100 \
    --Offset 0 \
    --SubnetId 123123 \
    --UniqueVpcId vpc-jmaywf6r \
    --UniqueSubnetId subnet-xxxx
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
                "LocalZoneFlag": 0
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

