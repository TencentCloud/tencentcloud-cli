**Example 1: 用于获取vpc子网的详细信息**



Input: 

```
tccli vpc DescribeSubnetDetailInternal --cli-unfold-argument  \
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
        "DefaultFlag": 0,
        "VpcId": 16769060,
        "UniqueVpcId": "vpc-7zayowkt",
        "VpcDefaultFlag": 0,
        "VpcSubnet": "10.0.0.0",
        "Owner": "251197522",
        "UniqueSubnetId": "subnet-1ufvulum",
        "VpcMask": "255.255.0.0",
        "AclId": 95805,
        "SubnetId": 2007467,
        "UniqAclId": "acl-r762el0i",
        "CreateTime": "2021-05-10 15:40:12",
        "Subnet": "10.0.0.0",
        "DhcpFlag": 0,
        "Name": "test",
        "BroadcastFlag": 0,
        "RoutingTableId": 218501,
        "ZoneId": 100001,
        "VpcIntMask": 16,
        "VpcName": "cissytest",
        "IntMask": 24,
        "UniqueRoutingTableId": "rtb-jrti12do",
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

