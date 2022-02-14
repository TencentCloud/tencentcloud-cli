**Example 1: 删除DDoS防护的端口acl策略**



Input: 

```
tccli antiddos DeletePortAclConfig --cli-unfold-argument  \
    --InstanceId bgpip-00001001 \
    --AclConfig.ForwardProtocol tcp \
    --AclConfig.DPortStart 0 \
    --AclConfig.DPortEnd 65535 \
    --AclConfig.SPortStart 0 \
    --AclConfig.SPortEnd 65535 \
    --AclConfig.Action drop
```

Output: 
```
{
    "Response": {
        "RequestId": "b7739a1e-837d-4248-bf9f-16a9bf77db22"
    }
}
```

