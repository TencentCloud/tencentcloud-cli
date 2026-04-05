**Example 1: 创建图表组件**



Input: 

```
tccli wedata CreateWidget --cli-unfold-argument  \
    --WorkspaceId 11 \
    --DashboardAccessKey 23729993fc3445c91762487027897a766adb1eaab927f \
    --PageAccessKey 3abc5beb18ee47021762487037717af42481c2fc9deac \
    --PageLayouts create_layout01061 \
    --Widget.WidgetType cross \
    --Widget.CustomerRefId create_ref_id \
    --Widget.WidgetOption tiny_x_option_json_create_01061 \
    --PageVersion 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageInfo": {
                "CustomerRefId": "page-1762487036402",
                "DisplayName": "无标题页面 2",
                "PageAccessKey": "3abc5beb18ee47021762487037717af42481c2fc9deac",
                "PageLayout": "create_layout01061",
                "PageType": "PAGE_TYPE_NORMAL",
                "PageVersion": 11
            },
            "Widget": {
                "CustomerRefId": "create_ref_id",
                "WidgetAccessKey": "28a109ca9c2c425c17676711342039b9ba5e83bd3ab80",
                "WidgetOption": "tiny_x_option_json_create_01061",
                "WidgetRid": "",
                "WidgetType": "cross",
                "WidgetVersion": 0
            }
        },
        "RequestId": "cf5e1f79-9e7a-4277-9c0d-081fb8b2e9f6"
    }
}
```

