**Example 1: 直播审核创建词库**



Input: 

```
tccli live CreateAuditKeywordLib --cli-unfold-argument  \
    --MatchType ExactMatch \
    --Name 黄暴过滤 \
    --Suggestion Block \
    --Description 自定义词库
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "LibId": "4c49c04f-6617-4705-b3ff-bedce642bfcb"
    }
}
```

