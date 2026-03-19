**Example 1: 产品类型错误**



Input: 

```
tccli iotexplorer ActivateTWeTalk --cli-unfold-argument  \
    --ServiceType 1 \
    --DeviceIds HX3VWPFMVX_dev
```

Output: 
```
{
    "Response": {
        "FailureRecords": [
            {
                "DeviceId": "HX3VWPFMVX_dev",
                "ErrCode": 60009,
                "ErrMessage": "产品不是码音视频类型",
                "ExpireTime": 0
            }
        ],
        "SuccessRecords": [],
        "RequestId": "8c672b42-0846-4a28-966a-a327e9684d7f"
    }
}
```

