**Example 1: 查询 TWeSee 人脸详情**

查询指定人脸详情。

Input: 

```
tccli iotexplorer DescribeTWeSeeFace --cli-unfold-argument  \
    --ProductId PRODUCTID1 \
    --DeviceName dev001 \
    --ChannelId 0 \
    --FaceId face-cccccccc-dddd-eeee-ffff-000000000000
```

Output: 
```
{
    "Response": {
        "Face": {
            "FaceId": "face-cccccccc-dddd-eeee-ffff-000000000000",
            "PersonId": "person-66666666-7777-8888-9999-000000000000",
            "Source": 0,
            "IsPrototype": true,
            "TimestampMs": 1710000000123,
            "BoundingBox": [
                0.1,
                0.2,
                0.42,
                0.68
            ]
        },
        "RequestId": "req-describe-face-1"
    }
}
```

