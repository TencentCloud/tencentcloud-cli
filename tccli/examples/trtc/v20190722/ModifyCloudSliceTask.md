**Example 1: 修改云端切片任务**



Input: 

```
tccli trtc ModifyCloudSliceTask --cli-unfold-argument  \
    --SdkAppId 20010806 \
    --TaskId -nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ.. \
    --SubscribeStreamUserIds.SubscribeAudioUserIds 555
```

Output: 
```
{
    "Response": {
        "RequestId": "b4d09681-4413-4f21-972d-bba98422aa30",
        "TaskId": "-nHwQ8NU7t7Ps1bc3MXN7wTw1-BZVg7bbhyXLoK-mumNM6KipeAYnB3iUGIpBL-ajrCF-pd2AQ.."
    }
}
```

