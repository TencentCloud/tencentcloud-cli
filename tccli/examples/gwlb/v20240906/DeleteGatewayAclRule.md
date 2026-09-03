**Example 1: 按规则ID删除网关负载均衡ACL规则**

规则ID通过DescribeGatewayAclRules接口获取

Input: 

```
tccli gwlb DeleteGatewayAclRule --cli-unfold-argument  \
    --AclGroupId gwlbacl-0pii**** \
    --AclRuleIds 1024 1025
```

Output: 
```
{
    "Response": {
        "RequestId": "ef36d811-96c9-4a8b-b45b-56613700ef9c"
    }
}
```

**Example 2: 按规则内容删除网关负载均衡ACL规则**

为兼容存量用法保留，Type为in、out的规则只能用这种方式删除

Input: 

```
tccli gwlb DeleteGatewayAclRule --cli-unfold-argument  \
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

