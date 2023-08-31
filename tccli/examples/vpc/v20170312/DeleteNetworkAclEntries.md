**Example 1: 删除单条IPv4规则**

删除单条IPv4规则

Input: 

```
tccli vpc DeleteNetworkAclEntries --cli-unfold-argument  \
    --NetworkAclId acl-n8w3ppae \
    --NetworkAclEntrySet.Ingress.0.NetworkAclIpv4EntryId acli43-kl90bzxv \
    --NetworkAclEntrySet.Egress.0.NetworkAclIpv4EntryId acli43-25s6gffh
```

Output: 
```
{
    "Response": {
        "RequestId": "fed474df-e6c9-434e-8d07-0ce7e11e7315"
    }
}
```

