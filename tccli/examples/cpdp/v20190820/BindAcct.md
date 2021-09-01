**Example 1: 绑定银行卡请求示例**

用于子商户绑定提现银行卡场景。

Input: 

```
tccli cpdp BindAcct --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --SubAppId your_sub_app_id \
    --BindType 1 \
    --SettleAcctNo encrypted_account_no \
    --SettleAcctName encrypted_account_name \
    --SettleAcctType 1 \
    --Mobile encrypted_mobile_no \
    --IdType 1 \
    --IdCode encrypted_id_code \
    --AcctBranchName 银行名称 \
    --EiconBankBranchId 分行ID \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature
```

Output: 
```
{
    "Response": {
        "RequestId": "4899ec78-5374-4ab4-bc0c-d758126c77b1"
    }
}
```

