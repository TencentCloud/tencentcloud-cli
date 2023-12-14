**Example 1: 批量禁止域名更新**



Input: 

```
tccli domain UpdateProhibitionIntlBatch --cli-unfold-argument  \
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

