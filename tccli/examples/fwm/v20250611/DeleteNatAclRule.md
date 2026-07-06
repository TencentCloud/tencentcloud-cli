**Example 1: 删除 NAT 规则**



Input: 

```
tccli fwm DeleteNatAclRule --cli-unfold-argument  \
    --GroupId fwmrg_wrzekq94u7 \
    --RuleIds 50d186fd-6da7-4de3-acbc-8efea0272c76 3196fa67-1f2f-46a1-b341-75edfa5094d3
```

Output: 
```
{
    "Response": {
        "RequestId": "32178aa0-b534-4c2f-ac11-818765fb4179"
    }
}
```

