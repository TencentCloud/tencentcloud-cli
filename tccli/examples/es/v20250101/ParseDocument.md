**Example 1: 文档解析示例**



Input: 

```
tccli es ParseDocument --cli-unfold-argument  \
    --Document.FileType TXT \
    --Document.FileUrl  \
    --Document.FileContent data:text/plain;base64,SGVsbG8sIFdvcmxkIQ== \
    --ModelName doc-llm
```

Output: 
```
{
    "Response": {
        "RequestId": "7ab3fd45-61e7-4e5e-8194-b1997f67fc18",
        "Progress": "0",
        "DocumentParseResultUrl": "",
        "FailedPages": []
    }
}
```

