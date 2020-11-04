**Example 1: 获取订单示例**



Input: 

```
tccli billing DescribeDealsByCond --cli-unfold-argument  \
    --StartTime '2016-01-01 00:00:00'\
    --EndTime '2016-02-01 00:00:00'\
    --Offset 0\
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Deals": [
            {
                "OrderId": "20180806110065",
                "Status": 4,
                "Payer": "505515676",
                "CreateTime": "2018-08-06 15:21:23",
                "VoucherDecline": 0,
                "ProjectId": 0,
                "GoodsCategoryId": 100019,
                "RealTotalCost": 17000,
                "Creator": "505515676"
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

