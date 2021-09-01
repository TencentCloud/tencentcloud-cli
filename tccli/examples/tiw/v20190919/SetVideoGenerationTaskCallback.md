**Example 1: 设置录制视频生成回调地址**



Input: 

```
tccli tiw SetVideoGenerationTaskCallback --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --Callback https://example.com/videoGeneration/callback
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

