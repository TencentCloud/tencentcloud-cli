**Example 1: 创建 TWeSee 人员**

创建人员并关联已导入的人脸。

Input: 

```
tccli iotexplorer CreateTWeSeePerson --cli-unfold-argument  \
    --ProductId PRODUCTID1 \
    --DeviceName dev001 \
    --ChannelId 0 \
    --Name 爸爸 \
    --FaceIds face-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
```

Output: 
```
{
    "Response": {
        "Person": {
            "PersonId": "person-11111111-2222-3333-4444-555555555555",
            "Name": "爸爸",
            "Source": 1,
            "IsRemembered": true,
            "Faces": [
                {
                    "FaceId": "face-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "PersonId": "person-11111111-2222-3333-4444-555555555555",
                    "Source": 1,
                    "IsPrototype": true,
                    "TimestampMs": 1710000000123,
                    "BoundingBox": [
                        0.1,
                        0.2,
                        0.42,
                        0.68
                    ]
                }
            ]
        },
        "RequestId": "req-create-person-1"
    }
}
```

