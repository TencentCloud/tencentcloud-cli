**Example 1: 异步调用设备行为**



Input: 

```
tccli iotvideo CallDeviceActionAsync --cli-unfold-argument  \
    --DeviceName xxx_76854689_1 \
    --InputParams {"test_para1":22} \
    --ActionId test_action \
    --ProductId L78xxxxZ95
```

Output: 
```
{
    "Response": {
        "RequestId": "8b8a77a8-16f5-46a9-8456-0686c9420c7d",
        "ClientToken": "141812200::8b8a77a8-16f5-46a9-8456-0686c9420c7d",
        "Status": "Sent"
    }
}
```

