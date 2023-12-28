**Example 1: 查询商品列表**



Input: 

```
tccli trp DescribeProducts --cli-unfold-argument  \
    --Name  \
    --MerchantId  \
    --PageSize 10 \
    --PageNumber 1 \
    --CertState -1
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
                    "url1"
                ],
                "CreateTime": "2021-11-30T09:00:33.000Z",
                "UpdateTime": "2021-11-30T09:16:23.000Z",
                "Ext": {},
                "MerchantName": "demo",
                "CertState": -1
            },
            {
                "ProductId": "4girpwhw677zdo9c6t",
                "CorpId": 10000,
                "MerchantId": "0",
                "ProductCode": "4girpwhw677zdo9c6t",
                "Name": "demo",
                "Specification": "",
                "Remark": "",
                "Logo": [],
                "CreateTime": "2021-11-30T08:50:48.000Z",
                "UpdateTime": "2021-11-30T08:51:11.000Z",
                "Ext": {},
                "MerchantName": "",
                "CertState": -1
            }
        ],
        "TotalCount": 2,
        "RequestId": "fe9462f4-bded-4b52-a84a-27cf6b2b46b4"
    }
}
```

