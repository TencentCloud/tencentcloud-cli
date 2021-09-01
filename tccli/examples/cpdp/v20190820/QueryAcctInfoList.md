**Example 1: 开户列表信息查询请求示例**

开户列表信息查询请求示例

Input: 

```
tccli cpdp QueryAcctInfoList --cli-unfold-argument  \
    --MidasAppId your_midas_app_id \
    --SubMchId your_sub_mch_id \
    --QueryAcctBeginTime time \
    --QueryAcctEndTime time \
    --PageOffset 1 \
    --MidasSecretId your_midas_secret_id \
    --MidasSignature your_midas_signature
```

Output: 
```
{
    "Response": {
        "RequestId": "fd590936-acd7-440c-9ac5-b698bc0a5af0",
        "ResultCount": 1,
        "TotalCount": 1,
        "QueryAcctItems": []
    }
}
```

