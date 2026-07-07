**Example 1: 关联 WAF Guardrail 防护**



Input: 

```
tccli clb AssociateModelRouterGuardrails --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --Guardrails.0.Type WAF \
    --Guardrails.0.InstanceId waf_2kw60zgy0908e8j3 \
    --Guardrails.0.ServiceId waf_rule_abc123 \
    --Guardrails.0.InputCheckDepth 5
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

