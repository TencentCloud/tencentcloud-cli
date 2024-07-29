**Example 1: 开通成功**



Input: 

```
tccli iotexplorer CreateCloudStorageAIService --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --PackageId 1m_ev_hl
```

Output: 
```
{
    "Response": {
        "RequestId": "a9a9d232-01c0-494a-baa3-57c384463c3f",
        "OrderId": "3c189db8-4637-4f7d-aee5-9d6172c2c9ec"
    }
}
```

**Example 2: 开通失败：指定的设备不存在**



Input: 

```
tccli iotexplorer CreateCloudStorageAIService --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --PackageId 1m_ev_hl
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "设备未创建或已删除，请检查后重新操作"
        },
        "RequestId": "053656d4-7694-47c4-9ed3-1d853454f8c7"
    }
}
```

**Example 3: 开通失败：设备未开通云存套餐**

设备当前无生效的云存套餐，尝试开通云存 AI 套餐时开通失败

Input: 

```
tccli iotexplorer CreateCloudStorageAIService --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --PackageId 1m_ev_hl
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.CloudStoragePackageRequired",
            "Message": "需先开通云存套餐"
        },
        "RequestId": "4d85001c-1f75-486e-b96c-f75e37b2b9a9"
    }
}
```

**Example 4: 开通失败：云存套餐与云存 AI 套餐时长不匹配**

设备当前生效云存月套餐，尝试开通云存 AI 年套餐时开通失败

Input: 

```
tccli iotexplorer CreateCloudStorageAIService --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --PackageId 1y_ft_od
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnsupportedOperation.CloudStoragePackageTimeMismatch",
            "Message": "云存套餐与云存 AI 套餐时长不匹配"
        },
        "RequestId": "703a2a1d-1d7b-4625-a151-a985b17f32a5"
    }
}
```

**Example 5: 开通失败：云存套餐与云存 AI 套餐类型不匹配**

设备当前生效全时云存套餐，尝试开通事件云存 AI 套餐时开通失败

Input: 

```
tccli iotexplorer CreateCloudStorageAIService --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --PackageId 1m_ev_od
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnsupportedOperation.CloudStoragePackageTypeMismatch",
            "Message": "云存套餐与云存 AI 套餐类型不匹配"
        },
        "RequestId": "884a9ffd-426f-48bf-ab6a-79a5bb1631c1"
    }
}
```

**Example 6: 开通失败：云存 AI 套餐有效时长超过云存套餐的有效时长**

设备当前生效事件云存月套餐（过期时间为 2024年12月1日 00:00:00），且设备当前生效云存 AI 事件视频浓缩月套餐（过期时间同样为 2024年12月1日 00:00:00），尝试继续追加开通云存 AI 事件视频浓缩月套餐时开通失败

Input: 

```
tccli iotexplorer CreateCloudStorageAIService --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --PackageId 1m_ev_hl
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.CloudStorageAIPackageExpireTimeExceeded",
            "Message": "云存 AI 套餐生效时长不能超过当前云存套餐生效时长"
        },
        "RequestId": "4d85001c-1f75-486e-b96c-f75e37b2b9a9"
    }
}
```

