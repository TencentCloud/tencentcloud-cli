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
                "NewName": "",
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
                "StatusDesc": "导入成功",
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

**Example 2: 更新时间**

更新时间

Input: 

```
tccli lke ListDoc --cli-unfold-argument  \
    --BotBizId 2046432781641786304 \
    --PageNumber 1 \
    --PageSize 15 \
    --Query t \
    --Status 10 \
    --QueryType filename \
    --CateBizId 0 \
    --UpdateTime.Start 2026-04-15 00:00:00 \
    --UpdateTime.End 2026-04-29 23:59:59
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AttrLabels": [
                    {
                        "AttrBizId": "2047229851896103040",
                        "AttrKey": "lsOOuJiJ",
                        "AttrName": "朝代",
                        "Labels": [
                            {
                                "LabelBizId": "2047229851900297344",
                                "LabelName": "21世纪"
                            }
                        ],
                        "Source": 1
                    }
                ],
                "AttrRange": 2,
                "AttributeFlags": [],
                "CateBizId": "2047572762068238464",
                "CosUrl": "/corp/1747547736762744832/2046432781641786304/doc/GcpdluVjCRFkyiCkoKEX-2046433768792204096.txt",
                "CreateTime": "1776742812",
                "CustomerKnowledgeId": "",
                "DocBizId": "2046433795425184512",
                "DocCharSize": "5281062",
                "DocSize": "11027751",
                "EnableScope": 4,
                "ExpireEnd": "0",
                "ExpireStart": "1776742811",
                "FileName": "绝世唐门.txt",
                "FileType": "txt",
                "IsAllowDelete": true,
                "IsAllowEdit": true,
                "IsAllowRefer": true,
                "IsAllowRestart": true,
                "IsAllowRetry": false,
                "IsCreatedQa": false,
                "IsCreatingQa": false,
                "IsDeleted": false,
                "IsDeletedQa": false,
                "IsDisabled": false,
                "IsRefer": false,
                "NewName": "",
                "Processing": [],
                "QaNum": 0,
                "Reason": "",
                "ReferUrlType": 0,
                "Source": 0,
                "SourceDesc": "KeySourceFileImport",
                "StaffName": "coco测试11",
                "Status": 10,
                "StatusDesc": "导入完成",
                "UpdateTime": "1777260664",
                "WebUrl": ""
            }
        ],
        "Total": "2",
        "RequestId": "64291550-b4c9-46d8-bd8d-56cb52ce1421"
    }
}
```

