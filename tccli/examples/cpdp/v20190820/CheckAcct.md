**Example 1: 提现银行卡验证请求示例**



Input: 

```
tccli cpdp CheckAcct --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --SubAppId your_sub_app_id \
    --BindType 1 \
    --SettleAcctNo encrypted_settle_account_no \
    --CurrencyType RMB \
    --CurrencyUnit 1 \
    --CurrencyAmt 10000 \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature 
```

Output: 
```
{
    "Response": {
        "FrontSeqNo": "1910120069802835",
        "RequestId": "93c636b2-2455-466d-ad49-12ede650196a"
    }
}
```

