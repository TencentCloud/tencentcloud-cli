**Example 1: 获取订单示例**

获取订单示例

Input: 

```
tccli billing DescribeDealsByCond --cli-unfold-argument  \
    --EndTime 2016-02-01 00:00:00 \
    --Limit 20 \
    --StartTime 2016-01-01 00:00:00 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Deals": [
            {
                "GoodsCategoryId": 100019,
                "TimeSpan": 1,
                "Policy": 100,
                "Formula": "退款：xxxxx元，代金券不退（xxxxxxxx",
                "Status": 4,
                "SubProductCode": "sp_abc",
                "ResourceId": [
                    "ins-abscde"
                ],
                "Price": 0.0,
                "ProductInfo": [
                    {
                        "Name": "规格名称",
                        "Value": "规格值"
                    }
                ],
                "TotalCost": 0.0,
                "ProductCode": "p_abc",
                "Payer": "1007416710",
                "RealTotalCost": 17000,
                "ProjectId": 0,
                "BigDealId": "20220214710000851640801",
                "PayMode": "1",
                "RefReturnDeals": "",
                "Action": "purchase",
                "OrderId": "20220214710000851640811",
                "VoucherDecline": 0,
                "Creator": "1007416710",
                "ProductName": "xx商品",
                "Currency": "CNY",
                "SubProductName": "xx商品",
                "TimeUnit": "m",
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "c33d6ae6-c0de-4a55-8318-0950b5bdc79e"
    }
}
```

