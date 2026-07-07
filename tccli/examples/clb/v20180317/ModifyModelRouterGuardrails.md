**Example 1: 修改 WAF Guardrail 防护**



Input: 

```
tccli clb ModifyModelRouterGuardrails --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --Guardrails.0.GuardrailId gr-2x9k3ab1 \
    --Guardrails.0.InstanceId waf_2kw60zgy0908e8j3 \
    --Guardrails.0.ServiceId waf_rule_replaced \
    --Guardrails.0.InputCheckDepth 8
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

