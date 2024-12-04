**Example 1: 获取企业组织成员**



Input: 

```
tccli organization GetOrganizationMember --cli-unfold-argument  \
    --MemberUin 100000000001
```

Output: 
```
{
    "Response": {
        "Uin": 100000000001,
        "Name": "member_name",
        "Remark": "create member",
        "JoinTime": "2020-10-08 12:09:12",
        "NodeId": 1001,
        "NodeName": "node_name",
        "ParentNodeId": 101,
        "RequestId": "fae840be-2b30-47ae-93b7-df5610168eff"
    }
}
```

