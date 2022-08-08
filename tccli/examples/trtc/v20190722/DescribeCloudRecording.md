**Example 1: 查询SdkAppId 为 1234 TaskId 为 xx 的录制状态。**



Input: 

```
tccli trtc DescribeCloudRecording --cli-unfold-argument  \
    --TaskId xx \
    --SdkAppId 1234
```

Output: 
```
{
    "Response": {
        "Status": "InProgress",
        "StorageFileList": [],
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

