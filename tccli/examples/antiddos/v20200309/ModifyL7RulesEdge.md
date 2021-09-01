**Example 1: 修改L7转发规则**



Input: 

```
tccli antiddos ModifyL7RulesEdge --cli-unfold-argument  \
    --Rule.KeepTime 1 \
    --Rule.Status 1 \
    --Rule.Domain xx \
    --Rule.Protocol xx \
    --Rule.SourceType 1 \
    --Rule.RuleId xx \
    --Rule.CCThreshold 1 \
    --Rule.HttpsToHttpEnable 1 \
    --Rule.CCEnable 1 \
    --Rule.PrivateKey xx \
    --Rule.CertType 1 \
    --Rule.LbType 1 \
    --Rule.SourceList.0.Source xx \
    --Rule.SourceList.0.Weight 1 \
    --Rule.Cert xx \
    --Rule.CCLevel xx \
    --Rule.KeepEnable 1 \
    --Rule.RuleName xx \
    --Rule.CCStatus 1 \
    --Rule.VirtualPort 1 \
    --Rule.SSLId xx \
    --Id xx \
    --Business xx
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

