**Example 1: 查询文档详情**

查询文档详情

Input: 

```
tccli lkeap DescribeDoc --cli-unfold-argument  \
    --KnowledgeBaseId 4901991032 \
    --DocId 1830881178265519872
```

Output: 
```
{
    "Response": {
        "DocId": "1830881178265519872",
        "FileName": "product_manuals.docx",
        "RequestId": "bf318516-67a7-41df-9460-e581b4ecedbd",
        "Status": "Parsing"
    }
}
```

