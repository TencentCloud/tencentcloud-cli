**Example 1: 拉取推荐结果**



Input: 

```
tccli irp RecommendContent --cli-unfold-argument  \
    --SceneId 20787a_13428 \
    --ResponseTimeout 300 \
    --RecTraceId abab \
    --UserIdList.0.UserIdType 4 \
    --UserIdList.0.UserId f458988816c956727db5d9fd6a1e4b3d \
    --Bid d3f5718e_d5a9 \
    --CurrentItemId  \
    --PoolId  \
    --ItemCnt 2 \
    --ItemTypeRatio 
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "RecTraceId": "9588983c6db7a36734d628537fb26463",
        "DataList": [
            {
                "ItemId": "20220324V0843100",
                "Weight": 997121,
                "ItemType": 3,
                "Score": 6.1,
                "Keyword": ""
            },
            {
                "ItemId": "20210213V02U2J00",
                "Weight": 950815,
                "ItemType": 3,
                "Score": 6.1,
                "Keyword": ""
            }
        ]
    }
}
```

