**Example 1: 修改五元组优先级**



Input: 

```
tccli vpc ModifyNetworkAclQuintupleEntries --cli-unfold-argument  \
    --NetworkAclId acl-12345678 \
    --NetworkAclQuintupleSet.Ingress.0.Priority 3
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

