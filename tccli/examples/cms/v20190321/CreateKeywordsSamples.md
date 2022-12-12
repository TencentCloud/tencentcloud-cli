**Example 1: 创建关键词**



Input: 

```
tccli cms CreateKeywordsSamples --cli-unfold-argument  \
    --UserAppID xx \
    --UserSubUin xx \
    --UserKeywords.0.Content xx \
    --UserKeywords.0.Label xx \
    --LibID xx \
    --UserUin xx \
    --Type xx
```

Output: 
```
{
    "Response": {
        "DupInfos": [
            {
                "Content": "测试关键字",
                "ID": "1234",
                "CreateTime": "2020-12-10 13:00:00",
                "Label": "Sexy"
            }
        ],
        "SampleIDs": [
            "125"
        ],
        "RequestId": "123144214414"
    }
}
```

