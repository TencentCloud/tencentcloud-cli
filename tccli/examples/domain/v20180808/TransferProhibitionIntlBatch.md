**Example 1: 批量禁止域名转移**



Input: 

```
tccli domain TransferProhibitionIntlBatch --cli-unfold-argument  \
    --Domains xx \
    --Status True
```

Output: 
```
{
    "Response": {
        "LogId": 11111111,
        "RequestId": "xx"
    }
}
```

