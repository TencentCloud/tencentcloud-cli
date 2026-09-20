**Example 1: 直播审核创建关键词**



Input: 

```
tccli live CreateAuditKeywords --cli-unfold-argument  \
    --Keywords.0.Content content \
    --Keywords.0.Label 321 \
    --LibId 4c49c04f-6617-4705-b3ff-bedce642bfcb
```

Output: 
```
{
    "Response": {
        "DupInfos": [
            {
                "Content": "content",
                "KeywordId": "8454212",
                "CreateTime": "2018-11-29T19:00:00Z",
                "Label": "321"
            }
        ],
        "KeywordIds": [
            "4895545216621"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

