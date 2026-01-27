**Example 1: 创建版本保留规则**



Input: 

```
tccli tcr CreateTagRetentionRule --cli-unfold-argument  \
    --RegistryId tcr-40s86s0j \
    --NamespaceId 1 \
    --CronSetting manual \
    --AdvancedRuleItems.0.RetentionPolicy.Key latestPushedK \
    --AdvancedRuleItems.0.RetentionPolicy.Value 7 \
    --AdvancedRuleItems.0.TagFilter.Decoration matches \
    --AdvancedRuleItems.0.TagFilter.Pattern v* \
    --AdvancedRuleItems.0.RepositoryFilter.Decoration repoMatches \
    --AdvancedRuleItems.0.RepositoryFilter.Pattern test-* \
    --Disabled False
```

Output: 
```
{
    "Response": {
        "RequestId": "831c375a-0beb-4ed3-b3b9-33926ebc2a8b"
    }
}
```

