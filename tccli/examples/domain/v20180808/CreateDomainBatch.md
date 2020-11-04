**Example 1: 批量注册域名**



Input: 

```
tccli domain CreateDomainBatch --cli-unfold-argument  \
    --TemplateId 字符串\
    --Period 整型\
    --Domains 数组\
    --PayMode 整型
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

