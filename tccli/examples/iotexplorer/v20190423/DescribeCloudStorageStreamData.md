**Example 1: 获取设备图片流数据**



Input: 

```
tccli iotexplorer DescribeCloudStorageStreamData --cli-unfold-argument  \
    --DeviceName device \
    --StartTime 1660561529 \
    --ProductId product
```

Output: 
```
{
    "Response": {
        "VideoStream": "https://test.cos.ap-guangzhou.myqcloud.com/test.mjpg",
        "AudioStream": "https://test.cos.ap-guangzhou.myqcloud.com/test.aac",
        "RequestId": "test-id"
    }
}
```

