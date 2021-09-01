**Example 1: 查询私有CA绑定的产品列表**



Input: 

```
tccli iotcloud DescribePrivateCABindedProducts --cli-unfold-argument  \
    --CertName CertName \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Products": [
            {
                "ProductId": "XKFAWDE6LX",
                "ProductName": "psk"
            }
        ],
        "RequestId": "xxxxxxxxx"
    }
}
```

