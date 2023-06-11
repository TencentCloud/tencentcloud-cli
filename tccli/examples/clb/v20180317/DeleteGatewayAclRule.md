**Example 1: 删除网关负载均衡ACL规则**

删除网关负载均衡ACL规则

Input: 

```
tccli clb DeleteGatewayAclRule --cli-unfold-argument  \
    --AclGroupId gwlbacl-0piisgzs \
    --AclRules.0.Type in \
    --AclRules.0.VpcId vpc-b5oj927d \
    --AclRules.0.Action drop \
    --AclRules.0.SrcIp 10.0.0.0 \
    --AclRules.1.Type out \
    --AclRules.1.VpcId vpc-b5oj927d \
    --AclRules.1.Action bypass \
    --AclRules.1.DstIp 10.0.0.0 \
    --AclRules.2.Type all \
    --AclRules.2.VpcId all \
    --AclRules.2.Action drop \
    --AclRules.2.SrcIp 10.0.0.0 \
    --AclRules.2.Protocol tcp \
    --AclRules.3.Type all \
    --AclRules.3.VpcId vpc-b5oj927d \
    --AclRules.3.Action bypass \
    --AclRules.3.SrcIp 10.0.0.0 \
    --AclRules.3.DstIp 1.1.1.1 \
    --AclRules.3.SrcPort 80 \
    --AclRules.3.DstPort 80
```

Output: 
```
{
    "Response": {
        "RequestId": "ef36d811-96c9-4a8b-b45b-56613700ef9c"
    }
}
```

