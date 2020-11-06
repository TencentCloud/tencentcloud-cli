**Example 1: RecognizeTargetAudience**



Input: 

```
tccli taf RecognizeTargetAudience --cli-unfold-argument  \
    --BspData.Uid bfd81ee3ed27ad31c95ca75e21365973 \
    --BspData.AccountType 2 \
    --BspData.ModelIdList 5128 5129
```

Output: 
```
{
    "Response": {
        "BspDate": {
            "Code": 0,
            "Message": "OK",
            "ScoreList": [
                {
                    "ModelId": 5128,
                    "IsFound": 1,
                    "Score": 120
                },
                {
                    "ModelId": 5129,
                    "IsFound": 0,
                    "Score": 0
                }
            ]
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

