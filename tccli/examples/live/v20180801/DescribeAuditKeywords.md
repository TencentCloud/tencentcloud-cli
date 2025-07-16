**Example 1: 直播审核获取关键词**

直播审核获取关键词列表搜索。

Input: 

```
tccli live DescribeAuditKeywords --cli-unfold-argument  \
    --Limit 0 \
    --Offset 100 \
    --LibId 4c49c04f-6617-4705-b3ff-bedce642bfcb \
    --Content 
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Infos": [
            {
                "KeywordId": "415124487845454",
                "Content": "content-name",
                "CreateTime": "20240214",
                "Label": "12"
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

