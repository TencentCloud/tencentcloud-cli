**Example 1: 获取分级详情**



Input: 

```
tccli dsgc DescribeDSPALevelDetail --cli-unfold-argument  \
    --DspaId dspa-00001
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "LevelGroupId": 1,
                "LevelRiskScore": 1,
                "LevelId": 1,
                "LevelRiskName": "xx"
            },
            {
                "LevelGroupId": 1,
                "LevelRiskScore": 1,
                "LevelId": 1,
                "LevelRiskName": "xx"
            },
            {
                "LevelGroupId": 1,
                "LevelRiskScore": 1,
                "LevelId": 1,
                "LevelRiskName": "xx"
            }
        ],
        "RequestId": "xx",
        "TotalCount": 1
    }
}
```

