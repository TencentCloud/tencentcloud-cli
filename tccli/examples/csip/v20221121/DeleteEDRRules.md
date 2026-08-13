**Example 1: 删除EDR策略**



Input: 

```
tccli csip DeleteEDRRules --cli-unfold-argument  \
    --RuleIDs 6511568c-5c8a-4507-a07b-df9e52f9bc21 \
    --RuleType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "61ca9489-b2df-40cb-888f-4464a9da89b7"
    }
}
```

