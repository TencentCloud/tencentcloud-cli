**Example 1: 查询项目**



Input: 

```
tccli mps QueryProject --cli-unfold-argument  \
    --ProjectId 458f16b1-7da9-4a56-a841-78567c5bee48 \
    --ProjectName 斗破苍穹 \
    --Page 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CreatedAt": 1775011251,
                "Description": "玄幻题材有声剧",
                "ProjectId": "458f16b1-7da9-4a56-a841-78567c5bee48",
                "ProjectName": "斗破苍穹",
                "Speakers": [
                    {
                        "AgeGroup": "youth",
                        "Description": "主角萧炎",
                        "Gender": "male",
                        "NameTerms": [
                            {
                                "Dst": "萧炎",
                                "Src": "Xiao Yan"
                            }
                        ],
                        "SpeakerId": "xiao_yan",
                        "VoiceId": "voice_001"
                    }
                ],
                "TermBase": [
                    {
                        "Dst": "迦南学院",
                        "Src": "Canaan Academy"
                    }
                ],
                "UpdatedAt": 1775011251
            }
        ],
        "Total": 1,
        "RequestId": "7f1115a9-5cfa-4455-9800-d354ade736c5"
    }
}
```

