**Example 1: 修改 TWeSee 人脸**

关联人脸并设置代表人脸状态。

Input: 

```
tccli iotexplorer ModifyTWeSeeFace --cli-unfold-argument  \
    --ProductId PRODUCTID1 \
    --DeviceName dev001 \
    --ChannelId 0 \
    --FaceId face-eeeeeeee-ffff-0000-1111-222222222222 \
    --PersonId person-11111111-2222-3333-4444-555555555555 \
    --IsPrototype False
```

Output: 
```
{
    "Response": {
        "Face": {
            "FaceId": "face-eeeeeeee-ffff-0000-1111-222222222222",
            "PersonId": "person-11111111-2222-3333-4444-555555555555",
            "Source": 1,
            "IsPrototype": false,
            "TimestampMs": 1710000000123,
            "BoundingBox": [
                0.12,
                0.18,
                0.48,
                0.72
            ]
        },
        "RequestId": "req-modify-face-1"
    }
}
```

