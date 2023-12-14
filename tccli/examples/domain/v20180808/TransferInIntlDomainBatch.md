**Example 1: 批量转入域名**



Input: 

```
tccli domain TransferInIntlDomainBatch --cli-unfold-argument  \
    --TemplateId abc \
    --PassWords abc \
    --Domains abc \
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

