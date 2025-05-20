**Example 1: 退还实例询价**



Input: 

```
tccli lighthouse InquirePriceIsolateInstances --cli-unfold-argument  \
    --InstanceIds lhins-f4flvxuh
```

Output: 
```
{
    "Response": {
        "InstanceRefundPriceSet": [
            {
                "InstanceId": "lhins-f4flvxuh",
                "RefundPrice": {
                    "RefundAmount": 98.0,
                    "RefundDetail": "退款：98元，现金券： 0元,代金券/折扣券不退（订单号20231020995000763739861：部件轻量应用服务器:现金支付54元=剩余54元;订单号20231020995000763770811：部件轻量应用服务器:现金支付40元-原价40*使用时间19.3548%=剩余32.26元;订单号20231020995000763883651：部件轻量应用服务器:现金支付14元-原价14*使用时间16.129%=剩余11.74元;"
                },
                "DiskRefundPriceSet": []
            }
        ],
        "TotalPrice": 98.0,
        "RequestId": "ce100397-ba85-40bb-ba90-ac951eb017f3"
    }
}
```

