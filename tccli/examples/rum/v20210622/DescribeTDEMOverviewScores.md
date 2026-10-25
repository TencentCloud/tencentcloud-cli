**Example 1: 查询总览分数**



Input: 

```
tccli rum DescribeTDEMOverviewScores --cli-unfold-argument  \
    --AppIds 7 \
    --StartTime 1787404860000 \
    --EndTime 1789996860000
```

Output: 
```
{
    "Response": {
        "Scores": [
            {
                "AppId": "7",
                "Items": [
                    {
                        "Key": "crash",
                        "Score": 0,
                        "Value": 0.03333333333333333
                    }
                ],
                "Platform": "iOS",
                "TotalScore": 6.8
            }
        ],
        "RequestId": "709cb6d7-0284-4cef-9e5b-fadaaafcf113"
    }
}
```

