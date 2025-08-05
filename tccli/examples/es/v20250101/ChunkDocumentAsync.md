**Example 1: 文档切片异步**



Input: 

```
tccli es ChunkDocumentAsync --cli-unfold-argument  \
    --Document.FileType TXT \
    --Document.FileUrl  \
    --Document.FileContent data:text/plain;base64,SGVsbG8sIFdvcmxkIQ== \
    --Document.FileName test.txt \
    --Document.FileStartPageNumber 1 \
    --Document.FileEndPageNumber 1 \
    --Config.MaxChunkSize 10000 \
    --ModelName doc-tree-chunk
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

