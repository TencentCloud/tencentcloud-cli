**Example 1: 批量域名续费**

批量域名续费

Input: 

```
tccli domain RenewDomainBatch --cli-unfold-argument  \
    --Period 1 \
    --Domains h101.dlgslb.cn h103.dlgslb.cn \
    --PayMode 1
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

