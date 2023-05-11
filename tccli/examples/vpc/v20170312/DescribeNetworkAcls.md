**Example 1: 示例1 查询网络ACL列表**

查询网络ACL列表

Input: 

```
tccli vpc DescribeNetworkAcls --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "NetworkAclSet": [
            {
                "TagSet": [],
                "NetworkAclId": "acl-kmxukyv6",
                "VpcId": "vpc-9it989fn",
                "NetworkAclType": "TRIPLE",
                "IngressEntries": [
                    {
                        "Protocol": "all",
                        "Description": "测试1",
                        "Ipv6CidrBlock": "::/0",
                        "ModifyTime": "2020-01-21 14:26:22",
                        "Action": "Drop",
                        "CidrBlock": "0.0.0.0/0",
                        "Port": "80"
                    }
                ],
                "SubnetSet": [
                    {
                        "NetworkAclId": "acl-kmxukyv6",
                        "RouteTableId": "rtb-we123456",
                        "VpcId": "vpc-rt123456",
                        "EnableBroadcast": true,
                        "Zone": "ap-guangzhou",
                        "Ipv6CidrBlock": "::/0",
                        "AvailableIpAddressCount": 1,
                        "IsRemoteVpcSnat": true,
                        "SubnetName": "子网1",
                        "TotalIpAddressCount": 1,
                        "IsCdcSubnet": 0,
                        "CdcId": "cluster-gbo27yc4",
                        "TagSet": [
                            {
                                "Value": "og",
                                "Key": "ck"
                            }
                        ],
                        "CreatedTime": "2020-01-20 14:26:22",
                        "SubnetId": "subnet-qmqye6ew",
                        "CidrBlock": "10.0.0.0/24",
                        "IsDefault": true
                    }
                ],
                "NetworkAclName": "测试001",
                "CreatedTime": "2020-01-20 14:26:22",
                "EgressEntries": [
                    {
                        "Protocol": "All",
                        "Description": "测试222",
                        "Ipv6CidrBlock": "::/0",
                        "ModifyTime": "2020-01-20 14:26:22",
                        "Action": "Drop",
                        "CidrBlock": "10.0.0.0/24",
                        "Port": "80"
                    }
                ]
            }
        ],
        "RequestId": "cccb2665-5d02-4d87-b9e7-757bb06e5beb"
    }
}
```

**Example 2: 示例2 根据条件查询网络ACL列表**

根据条件查询网络ACL列表

Input: 

```
tccli vpc DescribeNetworkAcls --cli-unfold-argument  \
    --NetworkAclIds acl-12345678 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "NetworkAclSet": [
            {
                "TagSet": [],
                "NetworkAclId": "",
                "VpcId": "vpc-kj123456",
                "NetworkAclType": "TRIPLE",
                "IngressEntries": [
                    {
                        "Protocol": "all",
                        "Description": "测试1",
                        "Ipv6CidrBlock": "::/0",
                        "ModifyTime": "2020-01-21 14:26:22",
                        "Action": "Drop",
                        "CidrBlock": "0.0.0.0/0",
                        "Port": "80"
                    }
                ],
                "SubnetSet": [
                    {
                        "NetworkAclId": "acl-kmxukyv6",
                        "RouteTableId": "rtb-we123456",
                        "VpcId": "vpc-kj123456",
                        "EnableBroadcast": true,
                        "Zone": "ap-guangzhou",
                        "Ipv6CidrBlock": "::/0",
                        "AvailableIpAddressCount": 1,
                        "IsCdcSubnet": 0,
                        "CdcId": "cluster-gbo27yc4",
                        "IsRemoteVpcSnat": true,
                        "SubnetName": "测试01",
                        "TotalIpAddressCount": 1,
                        "TagSet": [
                            {
                                "Value": "yt",
                                "Key": "kj"
                            }
                        ],
                        "CreatedTime": "2020-01-21 14:26:22",
                        "SubnetId": "subnet-qmqye6ew",
                        "CidrBlock": "10.0.0.0/24",
                        "IsDefault": true
                    }
                ],
                "NetworkAclName": "测试33",
                "CreatedTime": "2020-01-21 14:26:22",
                "EgressEntries": [
                    {
                        "Protocol": "All",
                        "Description": "测试",
                        "Ipv6CidrBlock": "::/0",
                        "ModifyTime": "2020-01-21 14:26:22",
                        "Action": "Drop",
                        "CidrBlock": "10.0.0.0/24",
                        "Port": "80"
                    }
                ]
            }
        ],
        "RequestId": "cccb2665-5d02-4d87-b9e7-757bb06e5beb"
    }
}
```

