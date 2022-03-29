**Example 1: 获取订单示例**



Input: 

```
tccli billing DescribeDealsByCond --cli-unfold-argument  \
    --StartTime '2016-01-01 00:00:00' \
    --EndTime '2016-02-01 00:00:00' \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Deals": [
            {
                "GoodsCategoryId": 100019,
                "TimeSpan": 0.0,
                "Policy": 0.0,
                "Formula": "xx",
                "Status": 4,
                "SubProductCode": "xx",
                "Price": 0.0,
                "ProductInfo": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "TotalCost": 0.0,
                "ProductCode": "xx",
                "Payer": "xx",
                "RealTotalCost": 17000,
                "ProjectId": 0,
                "BigDealId": "xx",
                "PayMode": "xx",
                "RefReturnDeals": "xx",
                "Action": "xx",
                "OrderId": "xx",
                "VoucherDecline": 0,
                "Creator": "xx",
                "ProductName": "xx",
                "Currency": "xx",
                "SubProductName": "xx",
                "TimeUnit": "xx",
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

