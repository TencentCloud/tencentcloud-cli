**Example 1: 创建热词列表示例**



Input: 

```
tccli trtc CreateRecognizeVocabV3 --cli-unfold-argument  \
    --Name 测试用户 \
    --SdkAppId 1400000001 \
    --WordWeights.0.Word 腾讯云 \
    --WordWeights.0.Weight 5
```

Output: 
```
{
    "Response": {
        "VocabId": "7bc538d6acb442f19dc3396dd7eacd66",
        "RequestId": "3196438f-39ef-47c0-98b8-8a50a7b4a313"
    }
}
```

