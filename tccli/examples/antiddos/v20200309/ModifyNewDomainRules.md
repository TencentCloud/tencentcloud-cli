**Example 1: 修改7层转发规则**



Input: 

```
tccli antiddos ModifyNewDomainRules --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Rule.RuleName name \
    --Rule.Protocol http \
    --Rule.Domain www.abc.com \
    --Rule.SourceType 2 \
    --Rule.LbType 1 \
    --Rule.KeepTime 300 \
    --Rule.SourceList.0.Source 1.1.1.10 \
    --Rule.SourceList.0.Weight 100 \
    --Rule.SourceList.1.Source 1.1.1.20 \
    --Rule.SourceList.1.Weight 100 \
    --Rule.CertType 0 \
    --Rule.VirtualPort 8443 \
    --Rule.KeepEnable 0
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

