**Example 1: 获取文档详情**



Input: 

```
tccli lke DescribeDoc --cli-unfold-argument  \
    --BotBizId 2082093730322742336 \
    --DocBizId 2082099064490625664 \
    --LoginUin None \
    --LoginSubAccountUin None
```

Output: 
```
{
    "Response": {
        "AttrLabels": [],
        "AttrRange": 1,
        "CateBizId": "2082093733996629248",
        "CateBizIdPath": [
            "0",
            "2082093733996629248"
        ],
        "CateNamePath": [
            "全部分类",
            "未分类"
        ],
        "CosUrl": "/corp/2082093552206806912/2082093730322742336/doc/BCkXkufxZByoRNWAeUpR-2082099021981876096.docx",
        "DocBizId": "2082099064490625664",
        "DocCharSize": "6105",
        "EnableScope": 2,
        "ExpireEnd": "0",
        "ExpireStart": "1785246074",
        "FileName": "故宫的宫殿介绍-老.docx",
        "FileType": "docx",
        "IsAllowDelete": true,
        "IsAllowEdit": true,
        "IsAllowRefer": true,
        "IsAllowRestart": true,
        "IsCreatedQa": false,
        "IsCreatingQa": false,
        "IsDeleted": false,
        "IsDeletedQa": false,
        "IsDisabled": false,
        "IsDownload": false,
        "IsRefer": false,
        "QaNum": 0,
        "Reason": "",
        "RequestId": "b8e56b01-a851-4991-9802-7ac409b60bdc",
        "Source": 0,
        "SourceDesc": "本地文档",
        "SplitRule": "{\"split_config_new\":{\"table_style\":\"md\",\"rm_spec_symbol\":1}}",
        "Status": 10,
        "StatusDesc": "导入完成",
        "UpdatePeriodInfo": {
            "UpdatePeriodH": 0
        },
        "UpdateTime": "1785246103"
    }
}
```

