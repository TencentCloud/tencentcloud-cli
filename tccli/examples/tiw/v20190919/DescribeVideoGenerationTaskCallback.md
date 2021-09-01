**Example 1: 查询录制视频生成回调地址**



Input: 

```
tccli tiw DescribeVideoGenerationTaskCallback --cli-unfold-argument  \
    --SdkAppId 1400000001
```

Output: 
```
{
    "Response": {
        "Callback": "https://example.com/offline/callback",
        "CallbackKey": "6vg9G7Fd",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

