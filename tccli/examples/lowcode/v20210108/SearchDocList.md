**Example 1: 知识库文档搜索接口**

根据关键字搜索知识库文档

Input: 

```
tccli lowcode SearchDocList --cli-unfold-argument  \
    --EnvId prod-1 \
    --CollectionView view \
    --SearchKey key \
    --SearchValue value \
    --PageNo 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "DocInfos": [
                {
                    "CollectionViewName": "name",
                    "DocSetId": "00-11",
                    "DocSetName": "abc.md",
                    "DocType": ".md",
                    "FileTitle": "title",
                    "FileMetaData": "{\"key\":\"value\"}",
                    "DocDesc": "test",
                    "FileSize": 0
                }
            ],
            "Total": 10
        },
        "RequestId": "1cc82948-244f-4812-bb2a-25a8a473d312"
    }
}
```

