**Example 1: 聚鑫-查询子账户绑定银行卡请求示例**

聚鑫-查询子账户绑定银行卡

Input: 

```
tccli cpdp QueryAcctBinding --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --SubAppId your_sub_mch_id \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature
```

Output: 
```
{
    "Response": {
        "RequestId": "fd590936-acd7-440c-9ac5-b698bc0a5af0",
        "TotalCount": 1,
        "BankCardItems": [
            {
                "IdType": "xx",
                "AcctBranchName": "xx",
                "Mobile": "xx",
                "SettleAcctType": 0,
                "CnapsBranchId": "xx",
                "BindType": 0,
                "IdCode": "xx",
                "SubAppId": "xx",
                "EiconBankBranchId": "xx",
                "SettleAcctName": "xx",
                "SettleAcctNo": "xx"
            }
        ]
    }
}
```

