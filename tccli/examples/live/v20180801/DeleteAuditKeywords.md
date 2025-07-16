**Example 1: 直播审核删除关键词**



Input: 

```
tccli live DeleteAuditKeywords --cli-unfold-argument  \
    --KeywordIds xx-id1 xx-id2 \
    --LibId 4c49c04f-6617-4705-b3ff-bedce642bfcb
```

Output: 
```
{
    "Response": {
        "SuccessCount": 100,
        "Infos": [
            {
                "KeywordId": "id1",
                "Deleted": true,
                "Content": "451id",
                "Error": "suc"
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

