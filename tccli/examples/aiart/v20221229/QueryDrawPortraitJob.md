**Example 1: 成功**

成功请求

Input: 

```
tccli aiart QueryDrawPortraitJob --cli-unfold-argument  \
    --JobId d33c2c966ae1476a5fae5e76
```

Output: 
```
{
    "Response": {
        "JobErrorCode": "",
        "JobErrorMsg": "",
        "JobStatusCode": "DONE",
        "JobStatusMsg": "处理完成",
        "RequestId": "9202070d-02bd-4848-bf54-568a2597e400",
        "ResultDetails": [
            "SUCCESS"
        ],
        "ResultUrls": [
            "https://aiart-portrait-xxx.cos.ap-guangzhou.myqcloud.com/xxx?q-sign-algorithm=sha1&q-ak=xxx&q-sign-time=1731996860;1732000460&q-key-time=1731996860;1732000460&q-header-list=host&q-url-param-list=&q-signature=2a86d7f0c5482e10d6867ddea14d9e3973201e95"
        ]
    }
}
```

