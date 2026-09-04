**Example 1: 查询词表列表示例**



Input: 

```
tccli trtc GetRecognizeVocabListV3 --cli-unfold-argument  \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VocabList": [
            {
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
                ]
            }
        ],
        "RequestId": "f612975e-4bca-4028-8eb6-d065f09f8345"
    }
}
```

