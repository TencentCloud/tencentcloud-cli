**Example 1: 创建关键词**

创建关键词

Input: 

```
tccli cms CreateKeywordsSamples --cli-unfold-argument  \
    --LibID abc \
    --UserKeywords.0.Content abc \
    --UserKeywords.0.Label abc \
    --UserKeywords.0.Remark abc \
    --UserKeywords.0.WordType abc
```

Output: 
```
{
    "Response": {
        "SampleIDs": [
            "abc"
        ],
        "SuccessInfos": [
            {
                "ID": "abc",
                "Content": "abc",
                "Label": "abc",
                "CreateTime": "abc",
                "Remark": "abc",
                "WordType": "abc"
            }
        ],
        "DupInfos": [
            {
                "ID": "abc",
                "Content": "abc",
                "Label": "abc",
                "CreateTime": "abc",
                "Remark": "abc",
                "WordType": "abc"
            }
        ],
        "InvalidSamples": [
            {
                "Content": "abc",
                "InvalidCode": 0,
                "InvalidMessage": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

