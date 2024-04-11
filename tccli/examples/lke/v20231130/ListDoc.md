**Example 1: 文档列表**



Input: 

```
tccli lke ListDoc --cli-unfold-argument  \
    --BotBizId 1727231073371148288 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AttrLabels": [],
                "AttrRange": 1,
                "CosUrl": "/corp/137/doc/jkadslfjalkdfjaklsdfla.docx",
                "DocBizId": "1729099536210460672",
                "DocCharSize": "5",
                "FileName": "jkadslfjalkdfjaklsdfla.docx",
                "FileType": "docx",
                "IsAllowDelete": true,
                "IsAllowEdit": true,
                "IsAllowRefer": true,
                "IsAllowRestart": true,
                "IsCreatedQa": true,
                "IsCreatingQa": false,
                "IsDeleted": false,
                "IsDeletedQa": false,
                "IsRefer": false,
                "QaNum": 2,
                "Reason": "生成问答成功",
                "Source": 1,
                "SourceDesc": "网页导入",
                "Status": 12,
                "StatusDesc": "已发布",
                "WebUrl": "",
                "ReferUrlType": 0,
                "UpdateTime": "1701425246"
            }
        ],
        "RequestId": "5526c65b-308d-4e84-b6b3-6b21d5c106b2",
        "Total": "1"
    }
}
```

