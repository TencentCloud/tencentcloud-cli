**Example 1: 查询rtb列表详情**



Input: 

```
tccli vpc DescribeRoutingTableListDetailInternal --cli-unfold-argument  \
    --Name xxx \
    --RoutingTableId 1 \
    --Limit 100 \
    --Offset 0 \
    --Owner 251198225 \
    --UniqueVpcId vpc-jmaywf6r
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RoutingTableSet": [
            {
                "Subnet": [
                    {
                        "Subnet": "172.16.0.0",
                        "Name": "Default-Subnet",
                        "CdcFlag": 0,
                        "DefaultFlag": 1,
                        "UniqueCdcId": "",
                        "Mask": "255.255.240.0",
                        "ZoneId": 100002,
                        "IntMask": 20,
                        "UniqueSubnetId": "subnet-dbrazzr0",
                        "SubnetId": 1990867,
                        "DhcpFlag": 0
                    }
                ],
                "VpcId": 78257,
                "Name": "default",
                "UniqueVpcId": "vpc-jmaywf6r",
                "SubnetNum": 1,
                "VpcSubnet": "172.16.0.0",
                "RoutingTableId": 213266,
                "RouterId": 196826,
                "VpcIntMask": 16,
                "VpcName": "Default-VPC",
                "VpcMask": "255.255.0.0",
                "VpcDefaultFlag": 1,
                "UniqueRouterId": "router-omlmjmr6",
                "Owner": "251198225",
                "UniqueRoutingTableId": "rtb-c6mxqnvy",
                "Type": 1,
                "CreateTime": "2021-03-22 20:59:55"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

