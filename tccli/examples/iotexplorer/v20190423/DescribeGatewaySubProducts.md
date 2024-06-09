**Example 1: 用于获取网关可绑定或解绑的子产品**



Input: 

```
tccli iotexplorer DescribeGatewaySubProducts --cli-unfold-argument  \
    --GatewayProductId M5QJPYQ \
    --ProjectId pri_211 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Products": [
            {
                "DevStatus": "1",
                "NetType": "wifi",
                "DataProtocol": 1,
                "ProjectId": "pro-jed",
                "ProductName": "名称",
                "ProductType": 0,
                "CategoryId": 0,
                "ProductId": "p_34rd",
                "ProductOwnerName": ""
            }
        ],
        "RequestId": "ed3-5tgbth565-678g"
    }
}
```

