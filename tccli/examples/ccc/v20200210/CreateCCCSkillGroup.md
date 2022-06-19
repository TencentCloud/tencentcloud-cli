**Example 1: 创建技能组实例**



Input: 

```
tccli ccc CreateCCCSkillGroup --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SkillGroupName “test” \
    --SkillGroupType 0 \
    --MaxConcurrency 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5ac74e13-ef15-41a6-9639-f1bc8c9896bd",
        "SkillGroupId": 602
    }
}
```

