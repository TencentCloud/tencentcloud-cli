**Example 1: 图表组件列表**



Input: 

```
tccli wedata ListWidgets --cli-unfold-argument  \
    --WorkspaceId 11 \
    --DashboardAccessKey 23729993fc3445c91762487027897a766adb1eaab927f \
    --PageAccessKey 3abc5beb18ee47021762487037717af42481c2fc9deac
```

Output: 
```
{
    "Response": {
        "Data": {
            "Widgets": [
                {
                    "CustomerRefId": "11073",
                    "WidgetAccessKey": "e100ed8b574048e217638095098119b7b18bceee30f4a",
                    "WidgetOption": "create_layout11072",
                    "WidgetRid": "",
                    "WidgetType": "Bar",
                    "WidgetVersion": 2
                }
            ]
        },
        "RequestId": "ec99a314-d2c5-4dfc-b6b2-328230140190"
    }
}
```

