**Example 1: 仪表盘导入**

仪表盘导入

Input: 

```
tccli wedata ImportApplicationDashboard --cli-unfold-argument  \
    --WorkspaceId 17625100163628872 \
    --FileUrl open/tcbi/wedata3-chatbi-server/updated-name-17222935-02ec-4047-bd6c-7c4a607a8369_1766579047427.json \
    --DisplayName test-export1766579048245
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessKey": "4771fc363fbb44681766579048795bf53cad3b75fff1a",
            "DashboardVersion": 0
        },
        "RequestId": "request_id"
    }
}
```

