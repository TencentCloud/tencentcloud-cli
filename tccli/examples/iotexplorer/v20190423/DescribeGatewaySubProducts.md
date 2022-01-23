**Example 1: 用于获取网关可绑定或解绑的子产品**



Input: 

```
tccli iotexplorer DescribeGatewaySubProducts --cli-unfold-argument  \
    --GatewayProductId M5QJPYQ \
    --Offset 0 \
    --Limit 10 \
    --ProjectId pri_211
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Products": [
            {
                "DevStatus": "xx",
                "NetType": "xx",
                "DataProtocol": 1,
                "ProjectId": "xx",
                "ProductName": "xx",
                "ProductType": 0,
                "CategoryId": 0,
                "ProductId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

