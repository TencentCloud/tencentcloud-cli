**Example 1: 退还云硬盘询价**



Input: 

```
tccli lighthouse InquirePriceIsolateDisks --cli-unfold-argument  \
    --DiskIds lhdisk-5wv5mklk
```

Output: 
```
{
    "Response": {
        "DiskRefundPriceSet": [
            {
                "DiskId": "lhdisk-5wv5mklk",
                "RefundPrice": {
                    "RefundAmount": 6.77,
                    "RefundDetail": "退款：6.77元，现金券： 0元,代金券/折扣券不退（订单号20231025995000773495711：部件云硬盘:现金支付7元-原价7*使用时间3.2258%=剩余6.77元;"
                }
            }
        ],
        "TotalPrice": 6.77,
        "RequestId": "9fa56411-0966-450a-bfa6-33321e23a211"
    }
}
```

