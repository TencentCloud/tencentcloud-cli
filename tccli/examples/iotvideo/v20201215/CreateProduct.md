**Example 1: 创建产品**



Input: 

```
tccli iotvideo CreateProduct --cli-unfold-argument  \
    --ProductDescription desc \
    --Features zxzj \
    --ChipId chip1 \
    --ProductName name \
    --DeviceType 1 \
    --ProductVaildYears 1 \
    --ChipManufactureId x86 \
    --ChipOs linux \
    --EncryptionType 2 \
    --NetType wifi
```

Output: 
```
{
    "Response": {
        "Data": {
            "UpdateTime": 1,
            "ProductDescription": "desc",
            "EncryptionType": 2,
            "ChipId": "chip1",
            "ProductName": "name",
            "DeviceType": 1,
            "ChipManufactureId": "x86",
            "ChipOs": "linux",
            "ProductId": "ZPDHQH7YHR",
            "CreateTime": 1612216201,
            "Features": [
                "zxzj"
            ],
            "NetType": "wifi",
            "CategoryId": 601
        },
        "RequestId": "055cdcffeed5"
    }
}
```

