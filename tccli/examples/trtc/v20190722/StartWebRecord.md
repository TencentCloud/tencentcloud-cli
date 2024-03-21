**Example 1: 启动一个页面录制任务**



Input: 

```
tccli trtc StartWebRecord --cli-unfold-argument  \
    --RecordUrl https://web-record-xxxxx.cos.ap-xxx.myqcloud.com/xxxx/xxx.mp4 \
    --StorageParams.CloudStorage.Vendor 0 \
    --StorageParams.CloudStorage.Bucket webrecord-1234589 \
    --StorageParams.CloudStorage.Region ap-chengdu \
    --StorageParams.CloudStorage.AccessKey AKxxxxxx \
    --StorageParams.CloudStorage.SecretKey Idxxxxxx \
    --StorageParams.CloudStorage.FileNamePrefix record video \
    --MaxDurationLimit 3600 \
    --WebRecordVideoParams.Width 1280 \
    --WebRecordVideoParams.Height 720 \
    --WebRecordVideoParams.Format mp4
```

Output: 
```
{
    "Response": {
        "TaskId": "abc",
        "RequestId": "abc"
    }
}
```

