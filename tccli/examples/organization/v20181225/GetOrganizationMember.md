**Example 1: Obtaining information on an organization member**



Input: 

```
tccli organization GetOrganizationMember --cli-unfold-argument  \
    --MemberUin 123
```

Output: 
```
{
    "Response": {
        "Uin": 1,
        "Name": "aa",
        "Remark": "",
        "JoinTime": "2019-10-10 00:00:00",
        "NodeId": 1,
        "NodeName": "aa",
        "ParentNodeId": 0,
        "RequestId": "fae840be-2b30-47ae-93b7-df5610168eff"
    }
}
```

