**Example 1: 查询成功**



Input: 

```
tccli hunyuan ListGlossary --cli-unfold-argument  \
    --Page 1 \
    --PageSize 2
```

Output: 
```
{
    "Response": {
        "Glossaries": [
            {
                "Description": "desc",
                "GlossaryId": "3177dfae1f8cb180dfcc1bea2ddf19f6",
                "Name": "My Glossary",
                "Source": "en",
                "Target": "zh"
            }
        ],
        "Page": 1,
        "PageSize": 2,
        "Total": 180,
        "RequestId": "68c98be9-3f46-4efa-9da9-3b5fc435527c"
    }
}
```

