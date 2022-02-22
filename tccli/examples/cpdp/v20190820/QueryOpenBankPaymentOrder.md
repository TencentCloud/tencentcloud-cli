**Example 1: 查询订单成功实例**

查询订单成功实例

Input: 

```
tccli cpdp QueryOpenBankPaymentOrder --cli-unfold-argument  \
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
            "OutOrderId": "test0039",
            "ChannelOrderId": "20220203575005249744556032"
        }
    }
}
```

**Example 2: 查询订单结果内部异常**



Input: 

```
tccli cpdp QueryOpenBankPaymentOrder --cli-unfold-argument  \
    --Environment 20220218580408557254664192 \
    --OutOrderId test202202180004 \
    --ChannelOrderId 字符串 \
    --ChannelMerchantId CM572433237990035456
```

Output: 
```
{
    "Response": {
        "RequestId": "77898adf-26af-4ac0-983c-d542ef6bacca",
        "Result": null,
        "ErrCode": "COMMON.SYSTEM_ERROR",
        "ErrMessage": "系统未知异常"
    }
}
```

