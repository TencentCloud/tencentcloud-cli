**Example 1: 查询商品列表**



Input: 

```
tccli trp DescribeProducts --cli-unfold-argument  \
    --Name 商品名称 \
    --MerchantId 商户ID \
    --PageSize 10 \
    --PageNumber 1 \
    --CertState 1
```

Output: 
```
{
    "Response": {
        "Products": [
            {
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
            }
        ],
        "TotalCount": 1,
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

