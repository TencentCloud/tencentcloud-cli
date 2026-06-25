**Example 1: 启动一个页面录制任务**



Input: 

```
tccli trtc StartWebRecord --cli-unfold-argument  \
    --RecordUrl https://webrtc-troubleshooting-demo-1258344699.cos-website.ap-guangzhou.myqcloud.com/whip-demos/test_webrecorder.html?video_count=1&video_resolution=720 \
    --StorageParams.CloudStorage.Vendor 0 \
    --StorageParams.CloudStorage.Region ap-nanjing \
    --StorageParams.CloudStorage.Bucket *************************************** \
    --StorageParams.CloudStorage.AccessKey ************************************ \
    --StorageParams.CloudStorage.SecretKey KN9espVu2tUoreAPN4UJr89tNaWDeqmR \
    --StorageParams.CloudStorage.FileNamePrefix isaaccheng \
    --SdkAppId 1400188366 \
    --WebRecordVideoParams.Width 1280 \
    --WebRecordVideoParams.Height 720 \
    --WebRecordVideoParams.Format mp4
```

Output: 
```
{
    "Response": {
        "TaskId": "N0VeWap2ZikvkBMy7vdQ2dHU-YweB2t48eNBquMyTewJWDH+GbjwpE1MLL9fuVSCWqv02VeJuL2IpqQ1dZArUQ66XwuZV7H9gK48N3nOnfGd0Vq78D-CkHWBmtvWbw..",
        "RequestId": "981dca49-afc8-4af7-9fa8-1d2408f94b8a"
    }
}
```

