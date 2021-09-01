**Example 1: 创建设备**

创建设备

Input: 

```
tccli iotexplorer CreateDevice --cli-unfold-argument  \
    --ProductId LJ0INDNU7Us \
    --DeviceName device2
```

Output: 
```
{
    "Response": {
        "Data": {
            "DeviceCert": "",
            "DeviceName": "device2",
            "DevicePrivateKey": "",
            "DevicePsk": "dvFeQr1zhBS2CDyYlN31XA=="
        },
        "RequestId": "fee15c53-91sac-488d-855d-c02d9f5f3d91"
    }
}
```

**Example 2: 创建 LoRa 设备**



Input: 

```
tccli iotexplorer CreateDevice --cli-unfold-argument  \
    --ProductId LJ0INDNU7U \
    --DeviceName light1 \
    --DevAddr 01865bd9 \
    --AppKey 00000000000000010000000000000001 \
    --DevEUI 0100000000000021 \
    --AppSKey bc97ea1ff62e7a3490135d989aae6bca \
    --NwkSKey bc97ea1ff62e7a3490135d989aae6bca
```

Output: 
```
{
    "Response": {
        "Data": {
            "DeviceCert": "",
            "DeviceName": "dd1",
            "DevicePrivateKey": "",
            "DevicePsk": "GTnp7I+yckhF3LrmHRtYBQ=="
        },
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e"
    }
}
```

**Example 3: 创建手动指定psk的设备**



Input: 

```
tccli iotexplorer CreateDevice --cli-unfold-argument  \
    --ProductId LJ0INDNU7Us \
    --DeviceName device2 \
    --DefinedPsk 1231
```

Output: 
```
{
    "Response": {
        "Data": {
            "DeviceCert": "",
            "DeviceName": "device2",
            "DevicePrivateKey": "",
            "DevicePsk": "1231"
        },
        "RequestId": "fee15c53-91sac-488d-855d-c02d9f5f3d91"
    }
}
```

