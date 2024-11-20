**Example 1: 查询文档拆分结果**

查询文档拆分结果

Input: 

```
tccli lkeap GetSplitDocumentResult --cli-unfold-argument  \
    --TaskId 236e51fd-827b-41cb-b303-56003a817ce5
```

Output: 
```
{
    "Response": {
        "DocumentRecognizeResultUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/example/example.zip",
        "RequestId": "ffe23ed8-2b64-4835-aedc-ca9a5b5a7384",
        "Status": "Success",
        "Usage": {
            "PageNumber": 10,
            "TotalTokens": 2048
        }
    }
}
```

