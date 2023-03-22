**Example 1: 批量域名续费**



Input: 

```
tccli domain RenewIntlDomainBatch --cli-unfold-argument  \
    --Domains test1.com test2.com \
    --Period 1 \
    --PayMode 1 \
    --AutoRenewFlag False
```

Output: 
```
{
    "Response": {
        "LogId": 4,
        "RequestId": "121323"
    }
}
```

