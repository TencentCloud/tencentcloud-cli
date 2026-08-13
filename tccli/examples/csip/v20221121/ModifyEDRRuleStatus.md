**Example 1: 开关EDR策略**



Input: 

```
tccli csip ModifyEDRRuleStatus --cli-unfold-argument  \
    --Status 1 \
    --RuleIDs 7b3313ed-0c7e-41c8-8ebd-94f4df1c96c9 \
    --RuleType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "459f304b-eb21-4011-b728-8797fd718ef9"
    }
}
```

