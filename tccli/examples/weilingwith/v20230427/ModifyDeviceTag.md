**Example 1: 修改设备标签**



Input: 

```
tccli weilingwith ModifyDeviceTag --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --Set.0.WID wid \
    --Set.0.NameSet name1 name2 \
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

