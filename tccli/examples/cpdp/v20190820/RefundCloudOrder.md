**Example 1: 聚鑫-退款申请**



Input: 

```
tccli cpdp RefundCloudOrder --cli-unfold-argument  \
    --TotalRefundAmt 1 \
    --MidasEnvironment sandbox \
    --MidasAppId demo001 \
    --SubOrderRefundList.0.SubOutTradeNo 4805X1183110364415535792X \
    --SubOrderRefundList.0.PlatformRefundAmt 0 \
    --SubOrderRefundList.0.SubRefundId 545464656565656124 \
    --SubOrderRefundList.0.SubMchRefundAmt 1 \
    --SubOrderRefundList.0.RefundAmt 1 \
    --UserId 66661877211 \
    --MchRefundAmt 1 \
    --OutTradeNo 1183110364214208944 \
    --RefundNotifyUrl RefundNotifyUrl \
    --RefundId 545464656565656124
```

Output: 
```
{
    "Response": {
        "RequestId": "98faef15-832d-4402-9283-a6031f13d12e"
    }
}
```

