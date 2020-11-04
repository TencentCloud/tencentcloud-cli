**Example 1: 查询子网列表**



Input: 

```
tccli vpc DescribeSubnets --cli-unfold-argument  \
    --Version 2017-03-12\
    --Filters.0.Name subnet-name\
    --Filters.0.Values 默认广州二区子网\
    --Filters.1.Name vpc-id\
    --Filters.1.Values vpc-2at5y1pn\
    --Filters.2.Name subnet-id\
    --Filters.2.Values subnet-otu92seu\
    --Filters.3.Name cidr-block\
    --Filters.3.Values 172.16.16.0\
    --Filters.4.Name is-default\
    --Filters.4.Values true
```

Output: 
```
{
    "Response": {
        "SubnetSet": [
            {
                "VpcId": "vpc-2at5y1pn",
                "SubnetId": "subnet-otu92seu",
                "SubnetName": "默认广州二区子网",
                "CidrBlock": "172.16.16.0/20",
                "Ipv6CidrBlock": "3402:4e00:20:1201::/64",
                "IsDefault": true,
                "IsRemoteVpcSnat": false,
                "EnableBroadcast": false,
                "Zone": "ap-guangzhou-dev-2",
                "RouteTableId": "rtb-l2h8d7c2",
                "TotalIpAddressCount": 4093,
                "AvailableIpAddressCount": 4002,
                "CreatedTime": "2017-04-20 11:30:48"
            }
        ],
        "TotalCount": 1,
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

**Example 2: 查询绑定了标签的子网列表**



Input: 

```
tccli vpc DescribeSubnets --cli-unfold-argument  \
    --Version 2017-03-12\
    --Filters.0.Name tag:city\
    --Filters.0.Values shanghai
```

Output: 
```
{
    "Response": {
        "SubnetSet": [
            {
                "VpcId": "vpc-2at5y1pn",
                "SubnetId": "subnet-otu92seu",
                "SubnetName": "默认广州二区子网",
                "CidrBlock": "172.16.16.0/20",
                "Ipv6CidrBlock": "3402:4e00:20:1201::/64",
                "IsDefault": true,
                "IsRemoteVpcSnat": false,
                "EnableBroadcast": false,
                "Zone": "ap-guangzhou-dev-2",
                "RouteTableId": "rtb-l2h8d7c2",
                "TotalIpAddressCount": 4093,
                "AvailableIpAddressCount": 4002,
                "TagSet": [
                    {
                        "Key": "city",
                        "Value": "shanghai"
                    }
                ],
                "CreatedTime": "2017-04-20 11:30:48"
            }
        ],
        "TotalCount": 1,
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

