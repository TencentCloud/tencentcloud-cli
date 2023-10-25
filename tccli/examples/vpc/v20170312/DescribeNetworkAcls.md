**Example 1: 示例1 查询网络ACL列表**

查询网络ACL列表

Input: 

```
tccli vpc DescribeNetworkAcls --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NetworkAclSet": [
            {
                "VpcId": "vpc-c1fd6eqe",
                "NetworkAclId": "acl-aeyasc3zz",
                "NetworkAclName": "ddd",
                "NetworkAclType": "1",
                "CreatedTime": "2021-02-19 17:52:43",
                "SubnetSet": [
                    {
                        "VpcId": "vpc-c1fd6eqe",
                        "SubnetId": "subnet-ptqwqcjzd",
                        "SubnetName": "test_3",
                        "CidrBlock": "10.0.0.0/24",
                        "IsDefault": true,
                        "EnableBroadcast": true,
                        "Zone": "ap-beijing",
                        "RouteTableId": "rtb-hnos32zkc",
                        "CreatedTime": "2021-02-19 17:52:43",
                        "AvailableIpAddressCount": 1,
                        "Ipv6CidrBlock": "",
                        "NetworkAclId": "acl-aeyasc3zz",
                        "IsRemoteVpcSnat": true,
                        "TotalIpAddressCount": 1,
                        "TagSet": [
                            {
                                "Key": "abc",
                                "Value": "abc"
                            }
                        ],
                        "CdcId": "cdc-12312",
                        "IsCdcSubnet": 0
                    }
                ],
                "IngressEntries": [
                    {
                        "Protocol": "all",
                        "Ipv6CidrBlock": "::/0",
                        "Action": "Accept",
                        "Description": "",
                        "ModifyTime": "",
                        "NetworkAclIpv6EntryId": "acli63-bwi12ozo",
                        "Priority": 1
                    }
                ],
                "EgressEntries": [
                    {
                        "Protocol": "all",
                        "Ipv6CidrBlock": "::/0",
                        "Action": "Accept",
                        "Description": "",
                        "ModifyTime": "",
                        "NetworkAclIpv6EntryId": "acli63-pmh23vc1q",
                        "Priority": 1
                    }
                ],
                "TagSet": [
                    {
                        "Key": "test",
                        "Value": "1"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

**Example 2: 示例2 根据条件查询网络ACL列表**

根据条件查询网络ACL列表

Input: 

```
tccli vpc DescribeNetworkAcls --cli-unfold-argument  \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-nwg3twqu \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NetworkAclSet": [
            {
                "VpcId": "vpc-nwg3twqu",
                "NetworkAclId": "acl-3v122sn",
                "NetworkAclName": "111111",
                "NetworkAclType": "TRIPLE",
                "CreatedTime": "2022-04-27 20:46:15",
                "TagSet": [],
                "SubnetSet": [],
                "IngressEntries": [
                    {
                        "Protocol": "all",
                        "Ipv6CidrBlock": "::/0",
                        "Action": "Drop",
                        "Description": "",
                        "ModifyTime": "",
                        "NetworkAclIpv6EntryId": "acli63-7whoqwek",
                        "Priority": 1
                    },
                    {
                        "Protocol": "all",
                        "CidrBlock": "172.16.0.0/16",
                        "Action": "Drop",
                        "Description": "",
                        "ModifyTime": "",
                        "NetworkAclIpv4EntryId": "acli43-dd0lxs1c",
                        "Priority": 1
                    },
                    {
                        "Protocol": "all",
                        "CidrBlock": "0.0.0.0/0",
                        "Action": "Drop",
                        "Description": "",
                        "ModifyTime": "",
                        "NetworkAclIpv4EntryId": "acli43-ezxjnhgy",
                        "Priority": 2
                    }
                ],
                "EgressEntries": [
                    {
                        "Protocol": "all",
                        "Ipv6CidrBlock": "::/0",
                        "Action": "Drop",
                        "Description": "",
                        "ModifyTime": "",
                        "NetworkAclIpv6EntryId": "acli63-pwqzahcs",
                        "Priority": 1
                    },
                    {
                        "Protocol": "all",
                        "CidrBlock": "0.0.0.0/0",
                        "Action": "Drop",
                        "Description": "",
                        "ModifyTime": "",
                        "NetworkAclIpv4EntryId": "acli43-ob44ewjm",
                        "Priority": 1
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "87c50ae4-bfd84-48cf-b92e-b637cewdd2aa"
    }
}
```

