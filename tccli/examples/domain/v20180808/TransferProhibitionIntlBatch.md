**Example 1: 批量禁止域名转移**



Input: 

```
tccli domain TransferProhibitionIntlBatch --cli-unfold-argument  \
    --Domains abc \
    --Status True
```

Output: 
```
{
    "Response": {
        "LogId": 0,
        "RequestId": "abc"
    }
}
```

