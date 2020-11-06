**Example 1: 创建产品**



Input: 

```
tccli iotvideo CreateProduct --cli-unfold-argument  \
    --ProductModel test \
    --ProductName TEST_001 \
    --ProductDescription TestProduct \
    --Features spdxth ypsxth
```

Output: 
```
{
    "Response": {
        "Data": {
            "ProductRegion": "xx",
            "ProductDescription": "xx",
            "ProductModel": "xx",
            "ProductName": "xx",
            "SecretKey": "xx",
            "FuncCode": [
                "xx"
            ],
            "IotModelRevision": 1,
            "ProductCate": 0,
            "CreateTime": 1,
            "ProductId": "xx"
        },
        "RequestId": "xx"
    }
}
```

