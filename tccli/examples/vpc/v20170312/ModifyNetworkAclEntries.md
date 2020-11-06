**Example 1: Deleting inbound rules of a network ACL**

To modify network ACL rules, you only need to pass in the rule you want to retain and discard the ones you want to delete. For example, the `acl-12345678` has two inbound rules:
* Rule 1: TCP 192.168.1.0/24 80 Accept
* Rule 2: TCP 192.168.1.0/24 443 Accept
<br/>If you want to delete the inbound rule 2, pass in parameters shown in the example.

Input: 

```
tccli vpc ModifyNetworkAclEntries --cli-unfold-argument  \
    --Version 2017-03-12 \
    --NetworkAclId acl-12345678 \
    --NetworkAclEntrySet.Ingress.0.Protocol TCP \
    --NetworkAclEntrySet.Ingress.0.Port 80 \
    --NetworkAclEntrySet.Ingress.0.CidrBlock 192.168.1.0/24 \
    --NetworkAclEntrySet.Ingress.0.Action Accept \
    --NetworkAclEntrySet.Ingress.0.Description test
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

**Example 2: Adding only inbound rules to a network ACL**



Input: 

```
tccli vpc ModifyNetworkAclEntries --cli-unfold-argument  \
    --Version 2017-03-12 \
    --NetworkAclId acl-12345678 \
    --NetworkAclEntrySet.Ingress.0.Protocol TCP \
    --NetworkAclEntrySet.Ingress.0.Port 80 \
    --NetworkAclEntrySet.Ingress.0.CidrBlock 192.168.1.0/24 \
    --NetworkAclEntrySet.Ingress.0.Action Accept \
    --NetworkAclEntrySet.Ingress.0.Description test \
    --NetworkAclEntrySet.Ingress.1.Protocol TCP \
    --NetworkAclEntrySet.Ingress.1.Port 442 \
    --NetworkAclEntrySet.Ingress.1.CidrBlock 192.168.1.0/24 \
    --NetworkAclEntrySet.Ingress.1.Action Accept \
    --NetworkAclEntrySet.Ingress.1.Description test
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

**Example 3: Adding inbound and outbound rules to a network ACL**

This example shows you how to delete an inbound rule. You need to pass in only the parameters of rules that you want to retain instead of specifying the rule to be deleted. For example, the instance `acl-12345678` has 2 inbound rules:
* Rule 1: TCP 192.168.1.0/24 80 Accept
* Rule 2: TCP 192.168.1.0/24 443 Accept
<br/>To delete Rule 2, specify the parameters as follows.

Input: 

```
tccli vpc ModifyNetworkAclEntries --cli-unfold-argument  \
    --Version 2017-03-12 \
    --NetworkAclId acl-12345678 \
    --NetworkAclEntrySet.Ingress.0.Protocol TCP \
    --NetworkAclEntrySet.Ingress.0.Port 80 \
    --NetworkAclEntrySet.Ingress.0.CidrBlock 192.168.1.0/24 \
    --NetworkAclEntrySet.Ingress.0.Action Accept \
    --NetworkAclEntrySet.Ingress.0.Description test \
    --NetworkAclEntrySet.Egress.0.Protocol TCP \
    --NetworkAclEntrySet.Egress.0.Port 80 \
    --NetworkAclEntrySet.Egress.0.CidrBlock 192.168.1.0/24 \
    --NetworkAclEntrySet.Egress.0.Action Accept \
    --NetworkAclEntrySet.Egress.0.Description test
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

