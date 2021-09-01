**Example 1: 批量域名注册**



Input: 

```
tccli domain CreateDomainBatch --cli-unfold-argument  \
    --Domains xx \
    --PayMode 0 \
    --Period 1 \
    --TemplateId xx
```

Output: 
```
{
    "Response": {
        "LogId": 318,
        "RequestId": "1684afa4-0bf7-49f8-a630-ab460e5c038e"
    },
    "ResultStatus": true
}
```

