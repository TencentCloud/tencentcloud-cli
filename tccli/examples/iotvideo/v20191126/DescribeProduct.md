**Example 1: 获取单个产品详细信息**



Input: 

```
tccli iotvideo DescribeProduct --cli-unfold-argument  \
    --ProductId 12345678910
```

Output: 
```
{
    "Response": {
        "Data": {
            "ProductId": "12345678910",
            "ProductModel": "test",
            "ProductName": "TEST_001",
            "ProductDescription": "TestProduct",
            "CreateTime": 1578295955,
            "IotModelRevision": 0,
            "SecretKey": "***********",
            "Features": [
                "ypsxth",
                "spdxth"
            ],
            "ChipManufactureId": "xxx",
            "ChipId": "xxx",
            "ProductCate": 1
        },
        "RequestId": "6869f8a5-c8f2-486d-ad94-67d74c97262a"
    }
}
```

