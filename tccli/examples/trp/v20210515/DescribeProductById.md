**Example 1: 查询商品信息**



Input: 

```
tccli trp DescribeProductById --cli-unfold-argument  \
    --ProductId eqdmnz7020bmtvi9
```

Output: 
```
{
    "Response": {
        "Product": {
            "ProductId": "85tfp1sn78r9m1568i",
            "CorpId": 10000,
            "MerchantId": "eqdmnz7020bmtvi9",
            "ProductCode": "85tfp1sn78r9m1568i",
            "Name": "demo5",
            "Specification": "100ml",
            "Remark": "desc",
            "Logo": [
                "https://xxx.xxx.com/logo.png"
            ],
            "CreateTime": "2021-11-30T09:00:33.000Z",
            "UpdateTime": "2021-11-30T09:16:23.000Z",
            "Ext": {
                "Value": "自定义"
            },
            "MerchantName": "demo",
            "CertState": 1
        },
        "RequestId": "06356857-6961-4b9d-bf1e-df5e0311358e"
    }
}
```

