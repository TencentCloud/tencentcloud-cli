**Example 1: 停止输入在线媒体流**

将SdkAppId为1234567890下的任务1234停止

Input: 

```
tccli trtc StopStreamIngest --cli-unfold-argument  \
    --SdkAppId 1234567890 \
    --TaskId 1234
```

Output: 
```
{
    "Response": {
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

