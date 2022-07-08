**Example 1: 同步调用设备行为**



Input: 

```
tccli iotvideo CallDeviceActionSync --cli-unfold-argument  \
    --DeviceName xxx_76854689_1 \
    --InputParams {"test_para1":22} \
    --ActionId test_action \
    --ProductId L78xxxxZ95
```

Output: 
```
{
    "Response": {
        "RequestId": "ea5f6542-3a2e-4bf7-8cac-11907e0a72a0",
        "ClientToken": "141812200::ea5f6542-3a2e-4bf7-8cac-11907e0a72a0",
        "OutputParams": "{\"test_res_para1\":3,\"test_res_para2\":5}",
        "Status": "success"
    }
}
```

