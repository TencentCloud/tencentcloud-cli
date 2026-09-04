**Example 1: 查询单个词表示例**



Input: 

```
tccli trtc GetRecognizeVocabV3 --cli-unfold-argument  \
    --VocabId 7bc538d6acb442f19dc3396dd7eacd66 \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "CreateTime": "2026-06-04T12:25:43+08:00",
        "Description": "",
        "Name": "测试用户",
        "State": 0,
        "UpdateTime": "2026-06-04T12:25:43+08:00",
        "VocabId": "7bc538d6acb442f19dc3396dd7eacd66",
        "WordWeights": [
            {
                "Weight": 5,
                "Word": "腾讯云"
            }
        ],
        "RequestId": "e0448aaa-e778-4495-b37a-32dc7475a7fd"
    }
}
```

