**Example 1: 更新版本保留规则**



Input: 

```
tccli tcr ModifyTagRetentionRule --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --RetentionId 1 \
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

**Example 2: 更新高级版本保留策略**



Input: 

```
tccli tcr ModifyTagRetentionRule --cli-unfold-argument  \
    --RegistryId tcr-40s86s0j \
    --NamespaceId 1 \
    --CronSetting manual \
    --RetentionId 2 \
    --AdvancedRuleItems.0.RetentionPolicy.Key latestPushedK \
    --AdvancedRuleItems.0.RetentionPolicy.Value 6 \
    --AdvancedRuleItems.0.TagFilter.Decoration matches \
    --AdvancedRuleItems.0.TagFilter.Pattern v \
    --AdvancedRuleItems.0.RepositoryFilter.Decoration repoMatches \
    --AdvancedRuleItems.0.RepositoryFilter.Pattern test-* \
    --Disabled False
```

Output: 
```
{
    "Response": {
        "RequestId": "adc30804-6a67-4e6b-8cdb-35f97f28b8df"
    }
}
```

