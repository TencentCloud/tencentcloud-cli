**Example 1: 用于申请IPv6地址**



Input: 

```
tccli vpc ApplyIpv6Internal --cli-unfold-argument  \
    --VpcId 1 \
    --IpType 41 \
    --SubnetAddress 2402:4e00:20:111:: \
    --Owner 2323232 \
    --Address 2402:4e00:20:111:0:8cce:1556:ccb9 \
    --SubnetId 1 \
    --SubnetIntPrefix 64 \
    --UniqueVpcId vpc-xxx \
    --UniqueSubnetId subnet-xxx
```

Output: 
```
{
    "Response": {
        "MappedMarkerId": "58.0.0.2",
        "VpcId": 79996,
        "IpType": 41,
        "UniqueVpcId": "vpc-r9u93oo3",
        "VpcIntPrefix": 56,
        "PublicIpFlag": 0,
        "SubnetAddress": "2402:4e00:1001:2f05::",
        "Flag": 1,
        "UniqueSubnetId": "subnet-9txzarp8",
        "VpcAddress": "2402:4e00:1001:2f00::",
        "Address": "2402:4e00:1001:2f05:0:96a8:110d:3589",
        "SubnetId": 1995599,
        "SubnetIntPrefix": 64,
        "CreateTime": "2022-06-29 14:57:27",
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

