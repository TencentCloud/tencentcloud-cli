**Example 1: 创建产品**



Input: 

```
tccli iotvideo CreateProduct --cli-unfold-argument  \
    --ProductVaildYears 5 \
    --ProductDescription binky_test \
    --EncryptionType 2 \
    --ChipId default \
    --ProductName test_lock6 \
    --DeviceType 1 \
    --NetType cellular \
    --ChipManufactureId default \
    --ChipOs default \
    --CategoryId 595 \
    --Features xxx
```

Output: 
```
{
    "Response": {
        "Data": {
            "ProductId": "L5N2BC8Q04",
            "ProductName": "test_lock6",
            "DeviceType": 1,
            "ProductVaildYears": 5,
            "EncryptionType": 2,
            "Features": [
                "unused"
            ],
            "CategoryId": 595,
            "ChipOs": "default",
            "ChipManufactureId": "default",
            "ChipId": "default",
            "ProductDescription": "binky_test",
            "NetType": "cellular",
            "CreateTime": 1661152125,
            "UpdateTime": 1661152125
        },
        "RequestId": "210e261e-5ab9-4b47-bfdf-68c63fb26a20"
    }
}
```

