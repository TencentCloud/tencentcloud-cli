**Example 1: 开户信息查询请求示例**

开户信息查询请求示例

Input: 

```
tccli cpdp QueryAcctInfo --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --SubMchId your_sub_mch_id \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature
```

Output: 
```
{
    "Response": {
        "RequestId": "fd590936-acd7-440c-9ac5-b698bc0a5af0",
        "SubAppId": "sub_app_id_used_for_payment",
        "SubAcctNo": "sub_account_no_from_bank"
    }
}
```

