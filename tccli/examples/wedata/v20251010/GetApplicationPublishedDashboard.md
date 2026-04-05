**Example 1: 获取仪表盘快照**



Input: 

```
tccli wedata GetApplicationPublishedDashboard --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --AccessKey 801469279624839168
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessKey": "801469279624839168",
            "DashboardVersion": 0,
            "DatasetOrderList": [
                "fb9e4d1f176889318086406b99645"
            ],
            "Datasets": [
                {
                    "Catalog": "",
                    "CustomSql": "",
                    "DataFrom": "SQL",
                    "DatasetVersion": 0,
                    "DatasourceType": "",
                    "Description": "",
                    "DisplayName": "无标题数据集2",
                    "FieldInfoList": [],
                    "Key": "e137c44917690013874604ff7c895",
                    "ModelType": "CUSTOM",
                    "ParameterList": [],
                    "Schema": "",
                    "TableName": ""
                }
            ],
            "DisplayName": "测试用例",
            "ExecuteResourceId": "res-123",
            "IsFavorite": false,
            "PageOrderList": [
                "e75774b91768893167246edb97d0f"
            ],
            "Pages": [
                {
                    "CustomerRefId": "fcd5c33670504d9c95c933caf5169b81",
                    "DisplayName": "无标题页面",
                    "PageAccessKey": "e75774b91768893167246edb97d0f",
                    "PageLayout": "[{\"i\":\"widget-2ca94e8d-afc6-4761-b0aa-1e35d4282651\",\"x\":2,\"y\":0,\"w\":3,\"h\":6,\"type\":\"bar\"}]",
                    "PageType": "PAGE_TYPE_NORMAL",
                    "PageVersion": 1,
                    "Widgets": [
                        {
                            "CustomerRefId": "widget-2ca94e8d-afc6-4761-b0aa-1e35d4282651",
                            "WidgetAccessKey": "255472c51769002273100749ff2b7",
                            "WidgetOption": "{\"visualization\":\"bar\",\"datasetName\":\"fb9e4d1f176889318086406b99645\",\"showAiAssistant\":true}",
                            "WidgetRid": "widget-2ca94e8d-afc6-4761-b0aa-1e35d4282651",
                            "WidgetType": "bar",
                            "WidgetVersion": 0
                        }
                    ]
                }
            ],
            "PublishTime": "1769002534238",
            "PublishUin": "700002164618",
            "UiSettings": ""
        },
        "RequestId": "72ff5ddb-c863-4228-b520-48a44196f649"
    }
}
```

