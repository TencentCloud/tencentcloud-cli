**Example 1: 获取产品详情**



Input: 

```
tccli iotvideo DescribeProduct --cli-unfold-argument  \
    --ProductId PTROMP3AOB
```

Output: 
```
{
    "Response": {
        "Data": {
            "ProductId": "PTROMP3AOB",
            "ProductName": "siva_003",
            "DeviceType": 1,
            "NetType": "xx",
            "EncryptionType": 2,
            "Features": [
                "ypsxth",
                "spdxth"
            ],
            "ChipOs": "Linux",
            "ChipManufactureId": "x86",
            "ChipId": "x86",
            "ProductDescription": "123",
            "CreateTime": 1608880525,
            "UpdateTime": 1611830563
        },
        "RequestId": "2172b7d1-9a49-4142-938a-ff4fa3d55881"
    }
}
```

