**Example 1: 添加网关负载均衡ACL规则**

同时添加Type为in、out、all的规则，其中Type为all的规则通过Priority指定优先级

Input: 

```
tccli gwlb AddGatewayAclRule --cli-unfold-argument  \
    --AclGroupId gwlbacl-0pii**** \
    --AclRules.0.Type in \
    --AclRules.0.VpcId vpc-b5oj**** \
    --AclRules.0.Action drop \
    --AclRules.0.SrcIp 10.0.0.0 \
    --AclRules.1.Type out \
    --AclRules.1.VpcId vpc-b5oj**** \
    --AclRules.1.Action bypass \
    --AclRules.1.DstIp 10.0.0.0 \
    --AclRules.2.Type all \
    --AclRules.2.VpcId all \
    --AclRules.2.Action drop \
    --AclRules.2.SrcIp 10.0.0.0 \
    --AclRules.2.Protocol tcp \
    --AclRules.2.Priority 1 \
    --AclRules.3.Type all \
    --AclRules.3.VpcId vpc-b5oj**** \
    --AclRules.3.Action bypass \
    --AclRules.3.SrcIp 10.0.0.0 \
    --AclRules.3.DstIp 1.1.1.1 \
    --AclRules.3.SrcPort 80 \
    --AclRules.3.DstPort 80 \
    --AclRules.3.Priority 2
```

Output: 
```
{
    "Response": {
        "RequestId": "39aeac6f-603b-4c1d-a3f0-d768599c8798"
    }
}
```

