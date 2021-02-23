**Example 1: 创建产品**



Input: 

```
tccli iotvideo CreateProduct --cli-unfold-argument  \
    --ProductDescription test \
    --Features test1 \
    --ChipId chip1 \
    --ProductName test \
    --DeviceType 1 \
    --ProductVaildYears 1 \
    --ChipManufactureId x86 \
    --ChipOs linux \
    --EncryptionType 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "UpdateTime": 1,
            "ProductDescription": "test",
            "EncryptionType": 2,
            "ChipId": "chip1",
            "ProductName": "test",
            "DeviceType": 1,
            "ChipManufactureId": "x86",
            "ChipOs": "linux",
            "ProductId": "ZPDHQH7YHR",
            "CreateTime": 1612216201,
            "Features": [
                "test1"
            ]
        },
        "RequestId": "055cdcffeed5"
    }
}
```

