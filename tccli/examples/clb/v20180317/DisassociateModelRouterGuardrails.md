**Example 1: 解除 WAF Guardrail 防护**



Input: 

```
tccli clb DisassociateModelRouterGuardrails --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --Guardrails.0.GuardrailId gr-2x9k3ab1
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

