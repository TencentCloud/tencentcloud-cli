**Example 1: ListDoc**



Input: 

```
tccli lke ListDoc --cli-unfold-argument  \
    --BotBizId ******98*********** \
    --PageNumber 1 \
    --PageSize 15 \
    --CateBizId 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AttrLabels": [],
                "AttrRange": 1,
                "AttributeFlags": [],
                "CateBizId": "2051219810371515712",
                "CosUrl": "******17475477*****7*******05121980*********2/*********R9CKlbRIcjWwvQB91*************",
                "CreateTime": "1780391506",
                "CustomerKnowledgeId": "",
                "DocBizId": "2061737527100798976",
                "DocCharSize": "738",
                "DocSize": "5001978",
                "EnableScope": 4,
                "ExpireEnd": "0",
                "ExpireStart": "1780391505",
                "FileName": "宝马.docx",
                "FileType": "docx",
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
                "IsRefer": true,
                "NewName": "",
                "Processing": [],
                "QaNum": 0,
                "Reason": "",
                "ReferUrlType": 0,
                "Source": 3,
                "SourceDesc": "腾讯云对象存储(COS)",
                "StaffName": "coco测试11",
                "Status": 10,
                "StatusDesc": "导入完成",
                "UpdateTime": "1780391614",
                "WebUrl": ""
            }
        ],
        "Total": "26",
        "RequestId": "240b7d9b-a068-4984-876f-6a17a388e26e"
    }
}
```

