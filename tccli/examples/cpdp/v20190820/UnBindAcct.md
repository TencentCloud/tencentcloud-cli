**Example 1: 解绑银行卡请求示例**

用于子商户解绑提现用银行的场景。

Input: 

```
tccli cpdp UnBindAcct --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --SubAppId your_sub_app_id \
    --SettleAcctNo encrypted_account_no \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature
```

Output: 
```
{
    "Response": {
        "RequestId": "51171073-5762-41af-a8a2-ccb291840539"
    }
}
```

