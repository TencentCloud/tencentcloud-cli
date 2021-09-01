**Example 1: 获取产品列表**



Input: 

```
tccli iotcloud DescribeProducts --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Products": [
            {
                "ProductId": "ABCDEF12345",
                "ProductName": "hello",
                "ProductMetadata": {
                    "CreationDate": 1529049275
                },
                "ProductProperties": {
                    "ProductDescription": "test",
                    "EncryptionType": "1",
                    "Region": "gz",
                    "ProductType": 0,
                    "Format": "json"
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "69f65618-600b-4ac4-b8e3-4528a6819078"
    }
}
```

