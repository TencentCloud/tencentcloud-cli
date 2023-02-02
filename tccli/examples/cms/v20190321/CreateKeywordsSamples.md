**Example 1: 创建关键词**

创建关键词

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
        "SampleIDs": [
            "xx"
        ],
        "DupInfos": [
            {
                "ID": "xx",
                "Content": "xx",
                "Label": "xx",
                "CreateTime": "xx",
                "Remark": "xx",
                "WordType": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

