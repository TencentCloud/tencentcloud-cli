**Example 1: 获取信息流推荐结果**



Input: 

```
tccli irp FeedRecommend --cli-unfold-argument  \
    --UserId 2824324234 \
    --InstanceId d3f5718e_d5a9 \
    --SceneId 20787a_13428 \
    --UserIdList.0.Type imei_md5 \
    --UserIdList.0.Value f458988816c956727db5d9fd6a1e4b3d \
    --ItemCnt 2 \
    --CurrentItemId 
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "DataList": [
            {
                "ItemId": "20220324V0843100",
                "ItemType": "article",
                "ItemTraceId": "9588983c6db7a36734d628537fb26463",
                "Score": 6.1
            },
            {
                "ItemId": "20210213V02U2J00",
                "ItemType": "article",
                "ItemTraceId": "9588983c6db7a36734d628537fb26463",
                "Score": 6.1
            }
        ]
    }
}
```

