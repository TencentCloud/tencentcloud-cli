**Example 1: 查询 WAF Guardrail 防护**



Input: 

```
tccli clb DescribeModelRouterGuardrails --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345
```

Output: 
```
{
    "Response": {
        "Guardrails": [
            {
                "GuardrailId": "gr-2x9k3ab1",
                "Type": "WAF",
                "InstanceId": "waf_2kw60zgy0908e8j3",
                "ServiceId": "waf_rule_abc123",
                "InputCheckDepth": 5
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

