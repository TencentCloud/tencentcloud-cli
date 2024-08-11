**Example 1: 更新任务**

更新SdkAppId为1234567890下的TaskId为1234的StreamUrl

Input: 

```
tccli trtc UpdateStreamIngest --cli-unfold-argument  \
    --SdkAppId 1234567890 \
    --TaskId 1234 \
    --StreamUrl https://a.b/test.mp4
```

Output: 
```
{
    "Response": {
        "Status": "InProgress",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

