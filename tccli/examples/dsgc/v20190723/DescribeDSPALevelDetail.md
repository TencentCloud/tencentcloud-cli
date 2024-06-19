**Example 1: 获取数据分级详情**

获取数据分级详情

Input: 

```
tccli dsgc DescribeDSPALevelDetail --cli-unfold-argument  \
    --DspaId dspa-7daf8fc9
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "LevelGroupId": 1,
                "LevelId": 1,
                "LevelRiskName": "高",
                "LevelRiskScore": 10
            },
            {
                "LevelGroupId": 1,
                "LevelId": 3,
                "LevelRiskName": "低",
                "LevelRiskScore": 1
            },
            {
                "LevelGroupId": 1,
                "LevelId": 2,
                "LevelRiskName": "中",
                "LevelRiskScore": 5
            }
        ],
        "RequestId": "0c92cb04-3ac8-477d-b77a-db6e248df728",
        "TotalCount": 3
    }
}
```

