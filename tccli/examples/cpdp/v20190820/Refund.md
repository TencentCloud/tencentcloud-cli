**Example 1: 退款请求示例**

用于订单退款场景。

Input: 

```
tccli cpdp Refund --cli-unfold-argument  \
    --UserId your_user_id \
    --RefundId testrefund10002 \
    --MidasAppId your_midas_app_id \
    --TotalRefundAmt 10 \
    --OutTradeNo order_no_10002 \
    --MchRefundAmt 9 \
    --PlatformRefundAmt 1 \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature \
    --SubOrderRefundList.0.PlatformRefundAmt 1 \
    --SubOrderRefundList.0.RefundAmt 10 \
    --SubOrderRefundList.0.SubMchRefundAmt 9 \
    --SubOrderRefundList.0.SubOutTradeNo sub_order_no_10002 \
    --SubOrderRefundList.0.SubRefundId sub_testrefund10002
```

Output: 
```
{
    "Response": {
        "RequestId": "43941f8c-270a-4b16-b385-44e772549c6c"
    }
}
```

