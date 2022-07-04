**Example 1: 获取VPC和Subnet信息**



Input: 

```
tccli vpc DescribeVpcAndSubnetInternal --cli-unfold-argument  \
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
        "VpcSet": [
            {
                "Subnet": "172.16.0.0",
                "SubnetSet": [
                    {
                        "Subnet": "172.16.0.0",
                        "Name": "Default-Subnet",
                        "DefaultFlag": 1,
                        "ZoneId": 100002,
                        "SubnetId": 1990867,
                        "UniqueSubnetId": "subnet-dbrazzr0",
                        "IntMask": 20,
                        "DhcpFlag": 0,
                        "CreateTime": "2021-03-22 20:59:55"
                    }
                ],
                "VpcId": 78257,
                "Name": "Default-VPC",
                "UniqueVpcId": "vpc-jmaywf6r",
                "DefaultFlag": 1,
                "IntMask": 16,
                "OwnedFlag": 0,
                "BraceLinkFlag": 0,
                "OwnerLevel": -1,
                "Owner": "251198225",
                "DhcpFlag": 1,
                "CreateTime": "2021-03-22 20:59:55"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

**Example 2: DescribeVpcAndSubnetInternal示例**



Input: 

```
tccli vpc DescribeVpcAndSubnetInternal --cli-unfold-argument  \
    --Owner 251198225 \
    --UniqueVpcId vpc-jmaywf6r \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "VpcSet": [
            {
                "Subnet": "172.16.0.0",
                "SubnetSet": [
                    {
                        "Subnet": "172.16.0.0",
                        "Name": "Default-Subnet",
                        "DefaultFlag": 1,
                        "ZoneId": 100002,
                        "SubnetId": 1990867,
                        "UniqueSubnetId": "subnet-dbrazzr0",
                        "IntMask": 20,
                        "DhcpFlag": 0,
                        "CreateTime": "2021-03-22 20:59:55"
                    }
                ],
                "VpcId": 78257,
                "Name": "Default-VPC",
                "UniqueVpcId": "vpc-jmaywf6r",
                "DefaultFlag": 1,
                "IntMask": 16,
                "OwnedFlag": 0,
                "BraceLinkFlag": 0,
                "OwnerLevel": -1,
                "Owner": "251198225",
                "DhcpFlag": 1,
                "CreateTime": "2021-03-22 20:59:55"
            }
        ],
        "RequestId": "55278dc2-fe4c-4e32-b3b8-3eb25740722d"
    }
}
```

