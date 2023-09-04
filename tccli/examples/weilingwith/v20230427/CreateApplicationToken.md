**Example 1: 获取应用凭证示例**



Input: 

```
tccli weilingwith CreateApplicationToken --cli-unfold-argument  \
    --ApplicationId 10001 \
    --Nonce e222d195-ab43-4b68-b115-0ad71488f7ed \
    --TenantId 10000 \
    --RequestTime 1693797989 \
    --Signature RDcVIT1tOqq5V3K0nnRjuTpFcVL8wlYb
```

Output: 
```
{
    "Response": {
        "Result": {
            "Token": "886c2341d97352aa027916ec0e0339fa"
        },
        "RequestId": "e222d195-ab43-4b68-b115-0ad71488f7ed"
    }
}
```

