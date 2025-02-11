**Example 1: 批量导入问答对**

批量导入问答对

Input: 

```
tccli lkeap ImportQAs --cli-unfold-argument  \
    --KnowledgeBaseId 4901991032 \
    --FileName qa_import.xlsx \
    --FileUrl https://xxx.cos.ap-guangzhou.myqcloud.com/file/qa_import.xlsx
```

Output: 
```
{
    "Response": {
        "RequestId": "21305ff4-94c7-4113-9977-9b20427e0a2a"
    }
}
```

