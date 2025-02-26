**Example 1: 获取知识库下文档详情**

获取知识库下文档详情

Input: 

```
tccli lowcode DescribeKnowledgeDocumentSetDetail --cli-unfold-argument  \
    --CollectionView gqtianTest222666 \
    --DocumentSetId 1248479222486937399296
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 1,
            "DocumentSet": {
                "DocumentSetId": "1248479222486937399296",
                "FileTitle": "kent测试文件",
                "FileMetaData": "{\"url\": \"https://ww.com\", \"total\": 3}",
                "DocumentSetInfo": {
                    "ByteLength": 46,
                    "CreateTime": "2024-06-07 11:31:45",
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
                "Text": "1. 入门微搭的技术文档\n2. 学习微搭",
                "TextPrefix": "1. 入门微搭的技术文档\n2. 学习微搭......"
            }
        },
        "RequestId": "b404ff44-6bc3-4f60-8185-2ff4d9be5b63"
    }
}
```

