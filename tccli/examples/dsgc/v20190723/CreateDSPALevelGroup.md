**Example 1: 新增分级**



Input: 

```
tccli dsgc CreateDSPALevelGroup --cli-unfold-argument  \
    --DspaId dspa-00000000 \
    --Name 系统-高中低 \
    --Description 系统默认分级 \
    --ItemLevels.0.LevelRiskName 高 \
    --ItemLevels.0.LevelRiskScore 10 \
    --ItemLevels.1.LevelRiskName 中 \
    --ItemLevels.1.LevelRiskScore 5 \
    --ItemLevels.2.LevelRiskName 低 \
    --ItemLevels.2.LevelRiskScore 1
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "LevelGroupId": 1
    }
}
```

