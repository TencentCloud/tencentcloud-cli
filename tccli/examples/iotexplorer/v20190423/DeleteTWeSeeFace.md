**Example 1: 删除 TWeSee 人脸**

删除指定人脸。

Input: 

```
tccli iotexplorer DeleteTWeSeeFace --cli-unfold-argument  \
    --ProductId PRODUCTID1 \
    --DeviceName dev001 \
    --ChannelId 0 \
    --FaceId face-dddddddd-eeee-ffff-0000-111111111111
```

Output: 
```
{
    "Response": {
        "RequestId": "req-delete-face-1"
    }
}
```

