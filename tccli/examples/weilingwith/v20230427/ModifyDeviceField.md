**Example 1: 修改设备自定义字段**



Input: 

```
tccli weilingwith ModifyDeviceField --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --Set.0.WID abc \
    --Set.0.Key size \
    --Set.0.Val 100 \
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

