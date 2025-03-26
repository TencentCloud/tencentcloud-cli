**Example 1: 创建产品**



Input: 

```
tccli iotvideo CreateProduct --cli-unfold-argument  \
    --ProductModel ipc \
    --ProductName dev-001 \
    --ProductDescription myProduct \
    --Features spdxth ypsxth
```

Output: 
```
{
    "Response": {
        "Data": {
            "ProductRegion": "ypsxth",
            "ProductDescription": "my ipc",
            "ProductModel": "ypsxth",
            "ProductName": "ypsxth",
            "SecretKey": "fdsfdhgdfg",
            "FuncCode": [
                "11"
            ],
            "IotModelRevision": 1,
            "ProductCate": 0,
            "CreateTime": 1,
            "ProductId": "6WD38Z392L"
        },
        "RequestId": "92406b3-5a9a-4fe8-bc43-45e3d794bb68"
    }
}
```

