**Example 1: 获取企业组织单元列表**



Input: 

```
tccli organization ListOrganizationNodes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Nodes": [
            {
                "NodeId": 1,
                "Name": "aa",
                "ParentNodeId": 111,
                "MemberCount": 11
            }
        ],
        "RequestId": "f2b75a7e-fc82-4b00-8426-d04371d9052c"
    }
}
```

