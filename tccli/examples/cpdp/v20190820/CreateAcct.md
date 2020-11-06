**Example 1: 子商户入驻请求示例**

用于子商户入驻的场景。

Input: 

```
tccli cpdp CreateAcct --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --SubMchId your_sub_mch_id \
    --SubMchName 商户名称 \
    --Address 商户地址 \
    --Contact encrypted_contact_information \
    --Mobile encrypted_mobile_no \
    --Email encrypted_email \
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

