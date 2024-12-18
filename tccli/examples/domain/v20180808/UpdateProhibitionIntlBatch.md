**Example 1: 批量禁止域名更新**



Input: 

```
tccli domain UpdateProhibitionIntlBatch --cli-unfold-argument  \
    --Domains test-a.com \
    --Status True
```

Output: 
```
{
    "Response": {
        "LogId": 0,
        "RequestId": "dwewr-fower-weqwe-focsd-fweqr"
    }
}
```

