**Example 1: 查询退款接口请求示例**

此接口适用于查询退款结果的场景。

Input: 

```
tccli cpdp QueryRefund --cli-unfold-argument  \
    --UserId your_user_id \
    --RefundId refund_id_00001 \
    --MidasAppId your_midas_app_id \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature
```

Output: 
```
{
    "Response": {
        "State": "2",
        "RequestId": "665464d4-67fc-4ca0-847e-183508710681"
    }
}
```

