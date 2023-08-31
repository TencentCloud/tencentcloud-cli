**Example 1: 增量增加三元组ACL规则。**

增量增加三元组ACL规则。

Input: 

```
tccli vpc CreateNetworkAclEntries --cli-unfold-argument  \
    --NetworkAclId acl-12345678 \
    --NetworkAclEntrySet.Ingress.0.Protocol TCP \
    --NetworkAclEntrySet.Ingress.0.Port 80 \
    --NetworkAclEntrySet.Ingress.0.CidrBlock 192.168.0.0/24 \
    --NetworkAclEntrySet.Ingress.0.Action Accept \
    --NetworkAclEntrySet.Ingress.0.Description TEST \
    --NetworkAclEntrySet.Egress.0.Protocol TCP \
    --NetworkAclEntrySet.Egress.0.Port 80 \
    --NetworkAclEntrySet.Egress.0.CidrBlock 192.168.0.0/24 \
    --NetworkAclEntrySet.Egress.0.Action Accept \
    --NetworkAclEntrySet.Egress.0.Description TEST
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

