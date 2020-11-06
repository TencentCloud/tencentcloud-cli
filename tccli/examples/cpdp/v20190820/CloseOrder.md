**Example 1: 关闭订单请求示例**

用于关闭未支付订单的场景，确保用户不会重复支付。

Input: 

```
tccli cpdp CloseOrder --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --OutTradeNo your_order_no \
    --UserId your_user_id \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature
```

Output: 
```
{
    "Response": {
        "RequestId": "43941f8c-270a-4b16-b385-44e772549c6c"
    }
}
```

