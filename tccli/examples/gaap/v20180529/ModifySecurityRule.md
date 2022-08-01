**Example 1: 修改规则名**



Input: 

```
tccli gaap ModifySecurityRule --cli-unfold-argument  \
    --Protocol TCP \
    --SourceCidr 180.180.180.180/8 \
    --RuleId sr-xxxx \
    --DestPortRange ALL \
    --AliasName t3 \
    --PolicyId sp-xxxx \
    --RuleAction ACCEPT
```

Output: 
```
{
    "Response": {
        "RequestId": "1eea4c85-e088-4512-9c6c-480dff91677e"
    }
}
```

