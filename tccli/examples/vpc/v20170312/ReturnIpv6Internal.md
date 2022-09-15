**Example 1: 用于退还IPv6地址**



Input: 

```
tccli vpc ReturnIpv6Internal --cli-unfold-argument  \
    --VpcId 1 \
    --SubnetId 1 \
    --Address 2402:4e00:20:111:0:8cce:1556:ccb9 \
    --Owner 121212 \
    --UniqueVpcId vpc-xxx \
    --DeletedFlag 1 \
    --UniqueSubnetId subnet-xxx
```

Output: 
```
{
    "Response": {
        "MappedMarkerId": "58.0.0.2",
        "VpcId": 79996,
        "UniqueVpcId": "vpc-r9u93oo3",
        "SubnetId": 1995599,
        "UniqueSubnetId": "subnet-9txzarp8",
        "Address": "2402:4e00:1001:2f05:0:96a8:110d:3589",
        "Owner": "251197522",
        "DeleteFlag": 1,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

