**Example 1: 查询知识库下文件集合**

查询知识库下文件集合

Input: 

```
tccli lowcode DescribeKnowledgeDocumentSetList --cli-unfold-argument  \
    --EnvId lowcode-2gay8jgh25c7b1cf \
    --CollectionView gqtianTest666 \
    --Query.Limit 10 \
    --Query.Offset 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 1,
            "DocumentSets": [
                {
                    "DocumentSetId": "1248479486937399296",
                    "FileTitle": "kent测试文件",
                    "FileMetaData": "{\"url\": \"https://ww.com\", \"total\": 3}",
                    "DocumentSetInfo": {
                        "ByteLength": 46,
                        "CreateTime": "2024-06-07 11:31:45",
                        "IndexedErrorMsg": "",
                        "IndexedProgress": 100,
                        "IndexedStatus": "Ready",
                        "Keywords": "",
                        "LastUpdateTime": "2024-06-07 11:31:46",
                        "TextLength": 20
                    },
                    "DocumentSetName": "jackzlqin.md",
                    "Name": "",
                    "Author": "",
                    "SplitterPreprocess": {
                        "AppendKeywordsToChunk": false,
                        "AppendTitleToChunk": true
                    },
                    "TextPrefix": "1. 入门微搭的技术文档\n2. 学习微搭......"
                }
            ]
        },
        "RequestId": "2e7bdcc4-d82f-4b81-abc6-6e8b08cf1832"
    }
}
```

