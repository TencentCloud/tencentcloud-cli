**Example 1: 文档详情**



Input: 

```
tccli lke DescribeDoc --cli-unfold-argument  \
    --BotBizId 1727231073371148288 \
    --DocBizId 1729099536210460672
```

Output: 
```
{
    "Response": {
        "RequestId": "17467eb0-3f01-4bc8-af86-3f3b6b01a40c",
        "IsAllowDelete": true,
        "IsCreatedQa": false,
        "IsDeleted": false,
        "SourceDesc": "网页导入",
        "UpdateTime": "1701427403",
        "DocBizId": "1729099536210460672",
        "DocCharSize": "5",
        "FileName": "jkadslfjalkdfjaklsdfla.docx",
        "IsAllowEdit": false,
        "IsDeletedQa": false,
        "AttrLabels": [],
        "AttrRange": 1,
        "CosUrl": "/corp/137/doc/jkadslfjalkdfjaklsdfla.docx",
        "IsAllowRefer": false,
        "IsCreatingQa": false,
        "Source": 1,
        "QaNum": 0,
        "Reason": "",
        "Status": 14,
        "StatusDesc": "学习失败",
        "FileType": "docx",
        "IsAllowRestart": true,
        "IsRefer": false
    }
}
```

