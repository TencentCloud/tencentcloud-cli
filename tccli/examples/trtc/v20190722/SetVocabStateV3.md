**Example 1: 设置默认词表/激活状态**

1=设为默认（激活），0=取消

Input: 

```
tccli trtc SetVocabStateV3 --cli-unfold-argument  \
    --VocabId 7bc538d6acb442f19dc3396dd7eacd66 \
    --State 1 \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "VocabId": "7bc538d6acb442f19dc3396dd7eacd66",
        "RequestId": "5032e115-d218-45af-8987-c8e2873db233"
    }
}
```

