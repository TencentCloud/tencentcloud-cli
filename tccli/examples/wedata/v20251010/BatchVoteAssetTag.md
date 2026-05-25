**Example 1: 资产打标**

给资产进行打标

Input: 

```
tccli wedata BatchVoteAssetTag --cli-unfold-argument  \
    --Votes.0.PropertyType catalog \
    --Votes.0.PropertyId 566 \
    --Votes.0.Tags.0.LabelId 27 \
    --Votes.0.Tags.0.LabelName label1 \
    --Votes.0.Tags.0.LabelValueId 53 \
    --Votes.0.Tags.0.LabelValue labelvalue1
```

Output: 
```
{
    "Response": {
        "Data": {
            "FailureCount": 0,
            "Results": [
                {
                    "Message": "成功",
                    "Success": true,
                    "VoteId": "0"
                }
            ],
            "SuccessCount": 1
        },
        "RequestId": "0dec0cb1-7d99-4537-82e5-089a01d01baa"
    }
}
```

