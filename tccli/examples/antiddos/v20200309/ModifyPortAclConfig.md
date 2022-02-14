**Example 1: 修改DDoS防护的端口acl策略**



Input: 

```
tccli antiddos ModifyPortAclConfig --cli-unfold-argument  \
    --InstanceId bgpip-00001001 \
    --OldAclConfig.ForwardProtocol tcp \
    --OldAclConfig.DPortStart 0 \
    --OldAclConfig.DPortEnd 65535 \
    --OldAclConfig.SPortStart 0 \
    --OldAclConfig.SPortEnd 65535 \
    --OldAclConfig.Action drop \
    --OldAclConfig.Priority 5 \
    --NewAclConfig.ForwardProtocol udp \
    --NewAclConfig.DPortStart 0 \
    --NewAclConfig.DPortEnd 65535 \
    --NewAclConfig.SPortStart 0 \
    --NewAclConfig.SPortEnd 65535 \
    --NewAclConfig.Action drop \
    --NewAclConfig.Priority 5
```

Output: 
```
{
    "Response": {
        "RequestId": "b7739a1e-837d-4248-bf9f-16a9bf77db22"
    }
}
```

