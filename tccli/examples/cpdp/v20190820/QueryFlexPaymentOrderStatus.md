**Example 1: 结算中心-查询提现单状态**



Input: 

```
tccli cpdp QueryFlexPaymentOrderStatus --cli-unfold-argument  \
    --OrderId 1524418188867043328
```

Output: 
```
{
    "Response": {
        "ErrCode": "0",
        "ErrMessage": "success",
        "Result": {
            "Status": "ACCEPTED",
            "StatusDesc": "已受理"
        },
        "RequestId": "46108f36-2dee-4674-b0df-920dbc54edf1"
    }
}
```

