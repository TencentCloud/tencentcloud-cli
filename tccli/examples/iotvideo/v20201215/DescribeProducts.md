**Example 1: 获取产品列表**



Input: 

```
tccli iotvideo DescribeProducts --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CategoryId": 113,
                "NetType": "wifi",
                "ProductId": "PTROMP3AOB",
                "ProductName": "siva_003",
                "DeviceType": 1,
                "EncryptionType": 2,
                "Features": [
                    "ypsxth",
                    "spdxth"
                ],
                "ChipOs": "Linux",
                "ChipManufactureId": "x86",
                "ChipId": "x86",
                "ProductDescription": "desc",
                "CreateTime": 1608880525,
                "UpdateTime": 1611830563
            },
            {
                "CategoryId": 113,
                "NetType": "wifi",
                "ProductId": "BPCJPETFZU",
                "ProductName": "test_siva_123",
                "DeviceType": 1,
                "EncryptionType": 2,
                "Features": [
                    "ypsxth",
                    "spdxth"
                ],
                "ChipOs": "Linux",
                "ChipManufactureId": "ak",
                "ChipId": "AK3918EV331",
                "ProductDescription": "dd12",
                "CreateTime": 1608786160,
                "UpdateTime": 1608868038
            }
        ],
        "TotalCount": 2,
        "RequestId": "bb92aaff-508b-4d10-8e42-5841e796ffda"
    }
}
```

