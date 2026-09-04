**Example 1: 更新词表**



Input: 

```
tccli trtc UpdateRecognizeVocabV3 --cli-unfold-argument  \
    --VocabId 7bc538d6acb442f19dc3396dd7eacd66 \
    --SdkAppId 1400000001 \
    --Description 描述文本 \
    --WordWeights.0.Word 腾讯云 \
    --WordWeights.0.Weight 10
```

Output: 
```
{
    "Response": {
        "VocabId": "7bc538d6acb442f19dc3396dd7eacd66",
        "RequestId": "6ed76420-65dc-4a75-a3b3-0e224ec2d050"
    }
}
```

