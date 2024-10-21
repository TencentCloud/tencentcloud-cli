**Example 1: 批量查询消息模板基本信息列表**



Input: 

```
tccli lowcode DescribeMessageTemplates --cli-unfold-argument  \
    --SearchTitleName abc \
    --PageNo 0 \
    --PageSize 0 \
    --EnvType abc \
    --TemplateId 1 \
    --EnvId abc \
    --TemplateType 0 \
    --AppCodeList abc \
    --DatasourceNameList abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "ResponseList": [
                {
                    "MessageTypeList": [
                        0
                    ],
                    "TemplateTitle": "abc",
                    "TemplateDesc": "abc",
                    "AppCode": "abc",
                    "Datasource": "abc",
                    "CreateBy": "abc",
                    "CreateTime": "2020-09-22 00:00:00",
                    "UpdateTime": "2020-09-22 00:00:00",
                    "TemplateId": 1,
                    "TemplateType": 0,
                    "DatasourceName": "abc",
                    "ViewId": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

