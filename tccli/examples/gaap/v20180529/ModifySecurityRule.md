**Example 1: 修改规则名**



Input: 

```
tccli gaap ModifySecurityRule --cli-unfold-argument  \
    --PolicyId sp-xxxx \
    --RuleId sr-xxxx \
    --AliasName t3 \
    --Protocol TCP \
    --SourceCidr 180.180.180.180/8 \
    --RuleAction ACCEPT \
    --DestPortRange ALL
```

Output: 
```
{
    "Response": {
        "RequestId": "1eea4c85-e088-4512-9c6c-480dff91677e"
    }
}
```

