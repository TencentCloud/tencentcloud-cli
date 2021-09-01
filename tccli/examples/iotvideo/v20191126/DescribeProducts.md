**Example 1: 获取产品列表**



Input: 

```
tccli iotvideo DescribeProducts --cli-unfold-argument  \
    --ProductModel test \
    --StartTime 1546272000 \
    --EndTime 1578298301 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Data": [
            {
                "ProductRegion": "xx",
                "ProductDescription": "xx",
                "Features": [
                    "ypsxth",
                    "spdxth"
                ],
                "ProductModel": "xx",
                "ChipId": "xx",
                "ProductName": "xx",
                "SecretKey": "xx",
                "ChipManufactureId": "xx",
                "IotModelRevision": 0,
                "ProductCate": 0,
                "CreateTime": 1578298201,
                "ProductId": "xx"
            },
            {
                "ProductRegion": "xx",
                "ProductDescription": "xx",
                "Features": [
                    "ypsxth",
                    "spdxth"
                ],
                "ProductModel": "xx",
                "ChipId": "xx",
                "ProductName": "xx",
                "SecretKey": "xx",
                "ChipManufactureId": "xx",
                "IotModelRevision": 0,
                "ProductId": "xx",
                "CreateTime": 1578298101,
                "ProductCate": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

