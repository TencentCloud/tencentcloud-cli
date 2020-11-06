**Example 1: 余额查询请求示例**

用于查询子商户的余额场景。

Input: 

```
tccli cpdp QueryBalance --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --SubAppId your_sub_app_id \
    --QueryFlag 2 \
    --PageOffset 0 \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature
```

Output: 
```
{
    "Response": {
        "QueryItems": [
            {
                "SubAcctNo": "your_sub_account_no",
                "SubAcctProperty": "1",
                "SubAcctName": "",
                "SubMchId": "your_sub_mch_id",
                "AcctAvailBal": "0.00",
                "CashAmt": "0.00",
                "MaintenanceDate": "20191011"
            }
        ],
        "StartRecordOffset": "1",
        "TotalCount": "1",
        "RequestId": "f4f8d200-34f6-4c1f-851f-8c1b3d4e9dba",
        "EndFlag": "1",
        "ResultCount": "1"
    }
}
```

