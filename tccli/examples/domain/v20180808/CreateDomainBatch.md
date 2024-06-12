**Example 1: 批量域名注册**



Input: 

```
tccli domain CreateDomainBatch --cli-unfold-argument  \
    --TemplateId tmpl-acxxxxxx \
    --Period 1 \
    --Domains abcd.xyz \
    --PayMode 0 \
    --AutoRenewFlag 0 \
    --PackageResourceId  \
    --UpdateProhibition 0 \
    --TransferProhibition 0 \
    --ChannelFrom ChannelFrom \
    --OrderFrom OrderFrom \
    --ActivityId 10001
```

Output: 
```
{
    "Response": {
        "LogId": 318,
        "RequestId": "1684afa4-0bf7-49f8-a630-ab460e5c038e"
    }
}
```

