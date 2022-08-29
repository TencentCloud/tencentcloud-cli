**Example 1: 用于查询IPv6子网段**



Input: 

```
tccli vpc DescribeIpv6SubnetInternal --cli-unfold-argument  \
    --VpcId 123123 \
    --VpcIntPrefix 60 \
    --Address 2402:4e00:20:111:: \
    --IntPrefix 64 \
    --Owner 251198225 \
    --PublicIpFlag 1 \
    --Limit 100 \
    --VpcAddress 2402:4e00:20:110:: \
    --Offset 0 \
    --SubnetId 123123 \
    --UniqueVpcId vpc-jmaywf6r \
    --UniqueSubnetId subnet-xxxx
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "Ipv6SubnetSet": [
            {
                "VpcId": 79996,
                "UniqueVpcId": "vpc-r9u93oo3",
                "VpcIntPrefix": 56,
                "PublicIpFlag": 0,
                "IntPrefix": 64,
                "SubnetId": 1995599,
                "UniqueSubnetId": "subnet-9txzarp8",
                "VpcAddress": "2402:4e00:1001:2f00::",
                "Address": "2402:4e00:1001:2f05::",
                "Owner": "251197522",
                "CreateTime": "2021-04-02 10:11:41"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

