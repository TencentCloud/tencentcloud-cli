**Example 1: 删除图表组件**



Input: 

```
tccli wedata DeleteWidget --cli-unfold-argument  \
    --WorkspaceId 11 \
    --DashboardAccessKey 23729993fc3445c91762487027897a766adb1eaab927f \
    --PageAccessKey 3abc5beb18ee47021762487037717af42481c2fc9deac \
    --WidgetAccessKey 0dd2a164ca10427f1763809495996bfc7b959ab769e4a \
    --PageVersion 8 \
    --PageLayouts delete0106
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
                "PageLayout": "delete0106",
                "PageType": "PAGE_TYPE_NORMAL",
                "PageVersion": 9
            }
        },
        "RequestId": "a93075a0-7e57-40ab-aaa8-5ceb1a524b31"
    }
}
```

