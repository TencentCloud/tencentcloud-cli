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
        "Data": {
            "Message": "xx",
            "Code": 0,
            "Value": [
                {
                    "IsFound": 0,
                    "Score": 0.0,
                    "ModelId": 1
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

