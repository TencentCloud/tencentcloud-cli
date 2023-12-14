**Example 1: 批量域名注册**



Input: 

```
tccli domain CreateDomainBatch --cli-unfold-argument  \
    --TemplateId abc \
    --Period 0 \
    --Domains abc \
    --PayMode 0 \
    --AutoRenewFlag 0 \
    --PackageResourceId abc \
    --UpdateProhibition 0 \
    --TransferProhibition 0 \
    --ChannelFrom abc \
    --OrderFrom abc \
    --ActivityId abc
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

