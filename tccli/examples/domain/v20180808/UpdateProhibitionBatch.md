**Example 1: 批量禁止域名更新**



Input: 

```
tccli domain UpdateProhibitionBatch --cli-unfold-argument  \
    --Domains h101.tencent.com \
    --Status True
```

Output: 
```
{
    "Response": {
        "LogId": 54,
        "RequestId": "ac64c5c2-c0f0-11ea-ba13-080027f4585e"
    }
}
```

