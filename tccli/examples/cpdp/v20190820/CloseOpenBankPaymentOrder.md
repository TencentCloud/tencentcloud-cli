**Example 1: 关闭订单成功示例**

关闭订单成功示例

Input: 

```
tccli cpdp CloseOpenBankPaymentOrder --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --OutOrderId test0039 \
    --ChannelOrderId 20220203575005249744556032
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {
            "OutOrderId": "test0039"
        }
    }
}
```

**Example 2: 关单订单不存在**



Input: 

```
tccli cpdp CloseOpenBankPaymentOrder --cli-unfold-argument  \
    --Environment 20220218580408557254664192 \
    --OutOrderId test202202180004 \
    --ChannelOrderId 字符串 \
    --ChannelMerchantId CM572433237990035456
```

Output: 
```
{
    "Response": {
        "RequestId": "3bee4957-16d7-4791-a829-664d27d4f22d",
        "Result": null,
        "ErrCode": "COMMON.RECORD_NOT_EXIST",
        "ErrMessage": "记录不存在:test202202180004"
    }
}
```

