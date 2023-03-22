**Example 1: 批量域名账号间转移**



Input: 

```
tccli domain ModifyOwnerIntlBatch --cli-unfold-argument  \
    --Domains test1.com test2.com \
    --ToUin 109619400 \
    --DnsTransfer True
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

