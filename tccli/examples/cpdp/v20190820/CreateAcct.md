**Example 1: 子商户入驻请求示例**

用于子商户入驻的场景。

Input: 

```
tccli cpdp CreateAcct --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --Mobile encrypted_mobile_no \
    --MidasSignature your_midas_signature \
    --MidasSecretId your_midas_secret_id \
    --SubMchName 商户名称 \
    --SubMchId your_sub_mch_id \
    --Contact encrypted_contact_information \
    --Address 商户地址 \
    --Email encrypted_email
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

