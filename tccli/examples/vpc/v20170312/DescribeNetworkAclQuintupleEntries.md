**Example 1: 示例1 根据条件查询网络ACL列表五元组条目**



Input: 

```
tccli vpc DescribeNetworkAclQuintupleEntries --cli-unfold-argument  \
    --NetworkAclId acl-hj3he929 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "NetworkAclQuintupleSet": [
            {
                "Protocol": "TCP",
                "Description": "demo",
                "SourcePort": "80",
                "SourceCidr": "192.168.0.0/24",
                "DestinationPort": "80",
                "DestinationCidr": "192.168.0.0/24",
                "Action": "ACCEPT",
                "CreateTime": "2019-11-11 22:16:17",
                "NetworkAclQuintupleEntryId": "acli45-q1phngkz",
                "NetworkAclDirection": "EGRESS",
                "Priority": 0
            }
        ],
        "RequestId": "cccb2665-5d02-4d87-b9e7-757bb06e5beb"
    }
}
```

