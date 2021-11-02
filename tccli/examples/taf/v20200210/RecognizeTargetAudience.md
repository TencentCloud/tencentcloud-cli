**Example 1: RecognizeTargetAudience**



Input: 

```
tccli taf RecognizeTargetAudience --cli-unfold-argument  \
    --BspData.Uid XXXXXXXXXXXXXXX \
    --BspData.AccountType 256 \
    --BspData.ModelIdList 5260 \
    --BspData.IsAuthorized 1
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

