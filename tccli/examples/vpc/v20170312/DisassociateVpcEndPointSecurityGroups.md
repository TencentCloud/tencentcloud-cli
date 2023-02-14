**Example 1: 终端节点解绑安全组**

终端节点解绑安全组

Input: 

```
tccli vpc DisassociateVpcEndPointSecurityGroups --cli-unfold-argument  \
    --EndPointId vpce-h0fk8lfc \
    --SecurityGroupIds sg-serghftg
```

Output: 
```
{
    "Response": {
        "RequestId": "7e6f5074-e4a2-4bb6-9cac-d2357a00896f"
    }
}
```

