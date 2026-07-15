**Example 1: 创建设备SDP应答**



Input: 

```
tccli iotexplorer CreateDeviceSDPAnswer --cli-unfold-argument  \
    --ProductId product \
    --DeviceName device \
    --SDPOffer v=0\r\no=- 1769412238477114228
```

Output: 
```
{
    "Response": {
        "SDPAnswer": "v=0\r\no=- 1769412238477114229",
        "RequestId": "0c4746c2-c06d-4849-a106-113956941993"
    }
}
```

