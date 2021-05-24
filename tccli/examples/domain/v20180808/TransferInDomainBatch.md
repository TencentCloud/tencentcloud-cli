**Example 1: 批量域名转入**



Input: 

```
tccli domain TransferInDomainBatch --cli-unfold-argument  \
    --TemplateId tmpl-xxxxx \
    --Domains h101.tencent.com \
    --PassWords 123456 \
    --PayMode 0
```

Output: 
```
{
    "Response": {
        "LogId": 54,
        "RequestId": "ac64c5c2-c0f0-11ea-ba13-080027f4585e"
    }
}
```

