**Example 1: 更新图表组件**



Input: 

```
tccli wedata UpdateWidget --cli-unfold-argument  \
    --WorkspaceId 11 \
    --DashboardAccessKey 23729993fc3445c91762487027897a766adb1eaab927f \
    --PageAccessKey 3abc5beb18ee47021762487037717af42481c2fc9deac \
    --Widget.WidgetAccessKey e100ed8b574048e217638095098119b7b18bceee30f4a \
    --Widget.WidgetVersion 1 \
    --Widget.WidgetType Bar \
    --Widget.CustomerRefId 11073 \
    --Widget.WidgetOption create_layout11072 \
    --PageVersion 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Widget": {
                "CustomerRefId": "11073",
                "WidgetAccessKey": "e100ed8b574048e217638095098119b7b18bceee30f4a",
                "WidgetOption": "create_layout11072",
                "WidgetRid": "",
                "WidgetType": "Bar",
                "WidgetVersion": 2
            }
        },
        "RequestId": "ea826165-7119-417e-8c35-8c09a7f39501"
    }
}
```

