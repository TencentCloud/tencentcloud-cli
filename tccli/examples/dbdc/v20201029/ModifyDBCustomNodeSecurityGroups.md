**Example 1: 修改节点安全组信息**

本接口（ModifyDBCustomNodeSecurityGroups）用于修改节点的安全组

Input: 

```
tccli dbdc ModifyDBCustomNodeSecurityGroups --cli-unfold-argument  \
    --NodeId dbcn-4ngxncm5 \
    --SecurityGroupIds sg-2nnt6fyf
```

Output: 
```
{
    "Response": {
        "RequestId": "1d49fd6b-b890-4926-a856-53a30a10e888"
    }
}
```

