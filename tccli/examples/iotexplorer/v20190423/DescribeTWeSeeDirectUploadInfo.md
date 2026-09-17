**Example 1: 查询 TWeSee 直传信息**

查询指定设备的视频理解单文件直传目录

Input: 

```
tccli iotexplorer DescribeTWeSeeDirectUploadInfo --cli-unfold-argument  \
    --ProductId default \
    --DeviceName dev001 \
    --ChannelId 0 \
    --ServiceType VID_COMP \
    --UploadTarget stream \
    --UploadMethod single
```

Output: 
```
{
    "Response": {
        "StorageRegion": "ap-guangzhou",
        "StorageBucket": "twesee-input-125*****99",
        "StoragePath": "Direct/*********711/vid-z1-s/",
        "COSURI": "cos://twesee-input-125*****99.ap-guangzhou/Direct/*********711/vid-z1-s/",
        "RequestId": "a0fc12a1-3196-4fa7-8125-10d29d52e8df"
    }
}
```

