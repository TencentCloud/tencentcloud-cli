**Example 1: 修改五元组优先级**



Input: 

```
tccli vpc CreateNetworkAclQuintupleEntries --cli-unfold-argument  \
    --NetworkAclId acl-irmuq4z4 \
    --NetworkAclQuintupleSet.Ingress.0.Protocol TCP \
    --NetworkAclQuintupleSet.Ingress.0.Description demo \
    --NetworkAclQuintupleSet.Ingress.0.DestinationCidr 192.168.0.0/24 \
    --NetworkAclQuintupleSet.Ingress.0.SourceCidr 192.168.0.0/24 \
    --NetworkAclQuintupleSet.Ingress.0.Action ACCEPT \
    --NetworkAclQuintupleSet.Ingress.0.DestinationPort 80 \
    --NetworkAclQuintupleSet.Ingress.0.SourcePort 80
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

