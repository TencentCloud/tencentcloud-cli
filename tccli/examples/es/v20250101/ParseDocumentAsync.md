**Example 1: 文件解析异步任务**



Input: 

```
tccli es ParseDocumentAsync --cli-unfold-argument  \
    --Document.FileType TXT \
    --Document.FileUrl  \
    --Document.FileContent data:text/plain;base64,SGVsbG8sIFdvcmxkIQ== \
    --Document.FileName test.txt \
    --ModelName doc-llm
```

Output: 
```
{
    "Response": {
        "RequestId": "e3a1a515-e53c-473f-9114-6d05a19d1c0c",
        "TaskId": "acf20b7e-47b2-4cfd-8aba-d170dee34cfc"
    }
}
```

