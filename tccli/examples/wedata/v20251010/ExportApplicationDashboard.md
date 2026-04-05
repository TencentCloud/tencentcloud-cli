**Example 1: 仪表盘导出**



Input: 

```
tccli wedata ExportApplicationDashboard --cli-unfold-argument  \
    --AccessKey 44348abac17148ca1764751310863a10b381c06903a3b \
    --WorkspaceId 17625100163628872
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessKey": "44348abac17148ca1764751310863a10b381c06903a3b",
            "DashboardVersion": 60,
            "FileUrl": "open/tcbi/wedata3-chatbi-server/700002164619/updated-name-17222935-02ec-4047-bd6c-7c4a607a8369_1766579047427.json",
            "DisplayName": "updated-name-17222935-02ec-4047-bd6c-7c4a607a8369"
        },
        "RequestId": "fb8502fa-0ef8-4831-bcd0-fb842dfdbce1"
    }
}
```

