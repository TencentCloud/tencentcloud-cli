**Example 1: 导入 TWeSee 人脸**

检测图片中的人脸。

Input: 

```
tccli iotexplorer ImportTWeSeeFaces --cli-unfold-argument  \
    --ProductId PRODUCTID1 \
    --DeviceName dev001 \
    --ChannelId 0 \
    --ImageURL https://example.com/photos/group.jpg
```

Output: 
```
{
    "Response": {
        "TaskId": "ft-123e4567-e89b-12d3-a456-426614174000",
        "Faces": [
            {
                "FaceId": "face-eeeeeeee-ffff-0000-1111-222222222222",
                "Source": 1,
                "IsPrototype": false,
                "TimestampMs": 1710000000123,
                "BoundingBox": [
                    0.1,
                    0.2,
                    0.3,
                    0.6
                ]
            }
        ],
        "RequestId": "req-import-faces-1"
    }
}
```

