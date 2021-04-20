**Example 1: 创建版本保留规则**



Input: 

```
tccli tcr CreateTagRetentionRule --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --NamespaceId 1 \
    --CronSetting weekly \
    --RetentionRule.Key latestPushedK \
    --RetentionRule.Value 20 \
    --Disabled true
```

Output: 
```
{
    "Response": {
        "RequestId": "c8bf292d-38c7-49d9-8da3-737d08160cfc"
    }
}
```

