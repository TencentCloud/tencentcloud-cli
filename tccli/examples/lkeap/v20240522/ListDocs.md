**Example 1: 获取文档列表**

获取文档列表

Input: 

```
tccli lkeap ListDocs --cli-unfold-argument  \
    --KnowledgeBaseId 4901991032 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "DocId": "1830985874053466048",
                "FileName": "product_manuals.docx",
                "Status": "Success"
            }
        ],
        "RequestId": "292da1b4-1125-4423-b7cd-5cf3b14eb98d",
        "TotalCount": 1
    }
}
```

