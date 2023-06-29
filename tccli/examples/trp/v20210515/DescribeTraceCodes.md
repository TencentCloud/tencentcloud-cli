**Example 1: 查询标识列表**



Input: 

```
tccli trp DescribeTraceCodes --cli-unfold-argument  \
    --Keyword xfetmgoiky2nms6nk8 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "TraceCodes": [
            {
                "Code": "https://anxin.m.qq.com/qr/eqdmnz7020bmtvi9_000243813742005003",
                "CorpId": 10000,
                "PackId": "z1vt4ma2jpladh362o",
                "BatchId": "xfetmgoiky2nms6nk8",
                "MerchantId": "eqdmnz7020bmtvi9",
                "ProductId": "85tfp1sn78r9m1568i",
                "Status": 0,
                "CreateTime": "2021-12-01T09:04:50.000Z",
                "UpdateTime": "2021-12-03T07:50:43.000Z",
                "MerchantName": "demo",
                "ProductName": "demo5"
            }
        ],
        "TotalCount": 4,
        "RequestId": "310c65d3-9be0-4d65-892c-fa09e9b69d25"
    }
}
```

