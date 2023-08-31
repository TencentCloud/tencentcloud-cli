**Example 1: 网络ACL添加入站规则和出站规则**

网络ACL添加入站规则和出站规则

Input: 

```
tccli vpc ModifyNetworkAclEntries --cli-unfold-argument  \
    --NetworkAclId acl-12345678 \
    --NetworkAclEntrySet.Ingress.0.Protocol TCP \
    --NetworkAclEntrySet.Ingress.0.Description test \
    --NetworkAclEntrySet.Ingress.0.Action Accept \
    --NetworkAclEntrySet.Ingress.0.CidrBlock 192.168.1.0/24 \
    --NetworkAclEntrySet.Ingress.0.Port 80 \
    --NetworkAclEntrySet.Egress.0.Protocol TCP \
    --NetworkAclEntrySet.Egress.0.Description test \
    --NetworkAclEntrySet.Egress.0.Action Accept \
    --NetworkAclEntrySet.Egress.0.CidrBlock 192.168.1.0/24 \
    --NetworkAclEntrySet.Egress.0.Port 80
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

**Example 2: 网络ACL只添加入站规则**

网络ACL只添加入站规则

Input: 

```
tccli vpc ModifyNetworkAclEntries --cli-unfold-argument  \
    --NetworkAclId acl-12345678 \
    --NetworkAclEntrySet.Ingress.0.Protocol TCP \
    --NetworkAclEntrySet.Ingress.0.Description test \
    --NetworkAclEntrySet.Ingress.0.Action Accept \
    --NetworkAclEntrySet.Ingress.0.CidrBlock 192.168.1.0/24 \
    --NetworkAclEntrySet.Ingress.0.Port 442 \
    --NetworkAclEntrySet.Ingress.1.Protocol TCP \
    --NetworkAclEntrySet.Ingress.1.Description test \
    --NetworkAclEntrySet.Ingress.1.Action Accept \
    --NetworkAclEntrySet.Ingress.1.CidrBlock 192.168.1.0/24 \
    --NetworkAclEntrySet.Ingress.1.Port 80
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

**Example 3: 网络ACL删除入站规则**

传参只传需要保留的规则，待删除的规则不传即可。比如实例acl-12345678当前有两条入站规则：
* 规则1：TCP 192.168.1.0/24 80 Accept
* 规则2：TCP 192.168.1.0/24 443 Accept
<br/>比如，此时需要删除入站规则2，按照下面实例传参。

Input: 

```
tccli vpc ModifyNetworkAclEntries --cli-unfold-argument  \
    --NetworkAclId acl-12345678 \
    --NetworkAclEntrySet.Ingress.0.Protocol TCP \
    --NetworkAclEntrySet.Ingress.0.Description test \
    --NetworkAclEntrySet.Ingress.0.Action Accept \
    --NetworkAclEntrySet.Ingress.0.CidrBlock 192.168.1.0/24 \
    --NetworkAclEntrySet.Ingress.0.Port 80
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

