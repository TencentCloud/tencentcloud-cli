**Example 1: RecognizeCustomizedAudience**



Input: 

```
tccli taf RecognizeCustomizedAudience --cli-unfold-argument  \
    --BspData.Uid bfd81ee3ed27ad31c95ca75e21365973 \
    --BspData.AccountType 2 \
    --BspData.ModelIdList 5128 5129
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": [
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
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

