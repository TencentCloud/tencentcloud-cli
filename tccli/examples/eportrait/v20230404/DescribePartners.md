**Example 1: DescribePartners1**

DescribePartners1

Input: 

```
tccli eportrait DescribePartners --cli-unfold-argument  \
    --Eid 4e8eb65c5f996b50e9b8e93be211a483 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Eid": "4e8eb65c5f996b50e9b8e93be211a483",
                "RealCapItems": [],
                "SeemStockPercent": "0",
                "ShouldCapItems": [
                    {
                        "InvestType": "货币",
                        "ShouldCap": "22000.0万元",
                        "ShouldCapDate": "2017-06-30"
                    }
                ],
                "StockName": "中霸集团有限公司",
                "StockPercent": 0,
                "StockType": "外国(地区)企业"
            }
        ],
        "RequestId": "d0539ed1-d1b5-4b64-8e63-23865e94cfcd",
        "TotalCount": 1
    }
}
```

