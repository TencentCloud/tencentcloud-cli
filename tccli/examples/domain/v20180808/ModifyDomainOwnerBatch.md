**Example 1: 域名过户**

域名批量过户

Input: 

```
tccli domain ModifyDomainOwnerBatch --cli-unfold-argument  \
    --Domains h101.tencent.com \
    --NewOwnerUin 123456
```

Output: 
```
{
    "Response": {
        "LogId": 425,
        "RequestId": "3c59eccc-efca-4109-1111-37e2e2bce25f"
    }
}
```

