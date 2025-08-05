**Example 1: 实时文档切片**



Input: 

```
tccli es ChunkDocument --cli-unfold-argument  \
    --Document.FileType TXT \
    --Document.FileContent 基于分隔符、文本长度进行切片，适用规则性较强的文本 \
    --ModelName doc-chunk \
    --Config.MaxChunkSize 4800 \
    --Config.Delimiters , \
    --Config.ChunkOverlap 4000
```

Output: 
```
{
    "Response": {
        "Chunks": [
            {
                "Content": "基于分隔符、文本长度进行切片，适用规则性较强的文本",
                "Index": 0
            }
        ],
        "Usage": {
            "TotalTokens": 17
        },
        "RequestId": "eeb0d39a-8a4a-431b-a577-2595202afaa1"
    }
}
```

