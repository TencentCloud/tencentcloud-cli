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
        "Status": "xx",
        "StorageFileList": [
            {
                "TrackType": "xx",
                "BeginTimeStamp": 1,
                "UserId": "xx",
                "FileName": "xx"
            }
        ],
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

