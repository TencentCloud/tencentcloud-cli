**Example 1: 停止云端录制**

停止SdkAppId 为 1234, TaskId 为 xx 的云端录制。

Input: 

```
tccli trtc DeleteCloudRecording --cli-unfold-argument  \
    --TaskId xx \
    --SdkAppId 1234
```

Output: 
```
{
    "Response": {
        "TaskId": "5df46eb2-8e4b-490e-9c3c-dbd3b84faefc",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

