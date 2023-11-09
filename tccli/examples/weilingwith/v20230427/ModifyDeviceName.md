**Example 1: 修改设备名字**

成功响应

Input: 

```
tccli weilingwith ModifyDeviceName --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --Set.0.WID be2ea997-b7f4-4167-9545-9aa275158a92 \
    --Set.0.DeviceName a \
    --ApplicationToken YVySZSL1Lp5UtSJ5uJVLJYOKDEGfCCH2
```

Output: 
```
{
    "Response": {
        "RequestId": "7ea50911-8e3d-40aa-82ee-c00d23cc044d",
        "Result": {
            "Msg": "ok"
        }
    }
}
```

