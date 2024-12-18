**Example 1: 批量转入域名**



Input: 

```
tccli domain TransferInIntlDomainBatch --cli-unfold-argument  \
    --TemplateId temp-dwerfdw \
    --PassWords password1 password2 \
    --Domains transfer-domain1.com transfer-domain2.com \
    --PayMode 0 \
    --AutoRenewFlag True \
    --TransferProhibition True \
    --UpdateProhibition True \
    --LockTransfer True
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

