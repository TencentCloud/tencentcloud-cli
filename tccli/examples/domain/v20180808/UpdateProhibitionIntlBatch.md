**Example 1: 批量禁止域名更新**



Input: 

```
tccli domain UpdateProhibitionIntlBatch --cli-unfold-argument  \
    --Domains xx \
    --Status True
```

Output: 
```
{
    "Response": {
        "LogId": 111,
        "RequestId": "xx"
    }
}
```

