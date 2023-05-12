**Example 1: 查询子网列表**

查询子网列表

Input: 

```
tccli vpc DescribeSubnets --cli-unfold-argument  \
    --Filters.0.Values vpc-2at5y1pn \
    --Filters.0.Name vpc-id \
    --Filters.1.Values 默认广州二区子网 \
    --Filters.1.Name subnet-name \
    --Filters.2.Values 172.16.16.0 \
    --Filters.2.Name cidr-block \
    --Filters.3.Values subnet-otu92seu \
    --Filters.3.Name subnet-id \
    --Filters.4.Values true \
    --Filters.4.Name is-default
```

Output: 
```
{
    "Response": {
        "SubnetSet": [
            {
                "NetworkAclId": "",
                "RouteTableId": "rtb-n0yr460a",
                "VpcId": "vpc-n0yr460a",
                "EnableBroadcast": false,
                "Zone": "ap-guangzhou",
                "Ipv6CidrBlock": "",
                "AvailableIpAddressCount": 1,
                "IsRemoteVpcSnat": false,
                "SubnetName": "子网1",
                "TotalIpAddressCount": 1,
                "IsCdcSubnet": 0,
                "CdcId": "cluster-1234dert",
                "TagSet": [
                    {
                        "Value": "ck",
                        "Key": "kc"
                    }
                ],
                "CreatedTime": "2020-05-25 20:09:07",
                "SubnetId": "subnet-bthucmmy",
                "CidrBlock": "10.0.0.0/16",
                "IsDefault": true
            }
        ],
        "TotalCount": 1,
        "RequestId": "cccb2665-5d02-4d87-b9e7-757bb06e5beb"
    }
}
```

**Example 2: 查询绑定了标签的子网列表**

查询绑定了标签的子网列表

Input: 

```
tccli vpc DescribeSubnets --cli-unfold-argument  \
    --Filters.0.Values shanghai \
    --Filters.0.Name tag:city
```

Output: 
```
{
    "Response": {
        "SubnetSet": [
            {
                "NetworkAclId": "",
                "RouteTableId": "rtb-n0yr460a",
                "VpcId": "vpc-n0yr460a",
                "EnableBroadcast": false,
                "Zone": "ap-guangzhou",
                "Ipv6CidrBlock": "2001::85b:3c51:f5ff:ffda",
                "AvailableIpAddressCount": 1,
                "IsRemoteVpcSnat": false,
                "SubnetName": "子网2",
                "TotalIpAddressCount": 1,
                "IsCdcSubnet": 0,
                "CdcId": "cluster-1234dert",
                "TagSet": [
                    {
                        "Value": "gt",
                        "Key": "ku"
                    }
                ],
                "CreatedTime": "2020-05-25 20:09:07",
                "SubnetId": "subnet-bthucmmy",
                "CidrBlock": "10.0.0.0/16",
                "IsDefault": true
            }
        ],
        "TotalCount": 1,
        "RequestId": "cccb2665-5d02-4d87-b9e7-757bb06e5beb"
    }
}
```

