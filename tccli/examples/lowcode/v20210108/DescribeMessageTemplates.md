**Example 1: 批量查询消息模板基本信息列表**



Input: 

```
tccli lowcode DescribeMessageTemplates --cli-unfold-argument  \
    --SearchTitleName xx \
    --EnvId env-001 \
    --PageNo 0 \
    --EnvType xx \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "ResponseList": [
                {
                    "AppCode": "string",
                    "CreateBy": "string",
                    "Datasource": "string",
                    "MessageTypeList": [
                        0
                    ],
                    "TemplateDesc": "string",
                    "TemplateId": 0,
                    "TemplateTitle": "string",
                    "CreateTime": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

