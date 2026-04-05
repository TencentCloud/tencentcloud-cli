**Example 1: 移动图表组件**



Input: 

```
tccli wedata MoveWidget --cli-unfold-argument  \
    --WorkspaceId 11 \
    --DashboardAccessKey 23729993fc3445c91762487027897a766adb1eaab927f \
    --PageAccessKey 3abc5beb18ee47021762487037717af42481c2fc9deac \
    --PageLayouts create_layout0106 \
    --PageVersion 9
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
                "PageLayout": "create_layout0106",
                "PageType": "PAGE_TYPE_NORMAL",
                "PageVersion": 10
            }
        },
        "RequestId": "f7bef01e-c9f2-4f6a-a951-b7f4cc767972"
    }
}
```

