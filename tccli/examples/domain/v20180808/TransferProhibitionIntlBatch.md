**Example 1: 批量禁止域名转移**



Input: 

```
tccli domain TransferProhibitionIntlBatch --cli-unfold-argument  \
    --Domains test-a.com \
    --Status True
```

Output: 
```
{
    "Response": {
        "LogId": 0,
        "RequestId": "seer-dwer-fewe-qwqwe-eweqw"
    }
}
```

