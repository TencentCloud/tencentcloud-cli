**Example 1: 批量添加DDoS防护的端口acl策略**



Input: 

```
tccli antiddos CreatePortAclConfigList --cli-unfold-argument  \
    --InstanceIdList bgpip-00001001 \
    --AclConfig.ForwardProtocol tcp \
    --AclConfig.DPortStart 0 \
    --AclConfig.DPortEnd 65535 \
    --AclConfig.SPortStart 0 \
    --AclConfig.SPortEnd 65535 \
    --AclConfig.Action drop \
    --AclConfig.Priority 10
```

Output: 
```
{
    "Response": {
        "RequestId": "b7739a1e-837d-4248-bf9f-16a9bf77db22"
    }
}
```

