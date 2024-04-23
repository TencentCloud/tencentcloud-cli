**Example 1: 成功**

成功请求

Input: 

```
tccli aiart QueryDrawPortraitJob --cli-unfold-argument  \
    --JobId abc
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
            "https://xxx.com/a.jpg"
        ]
    }
}
```

