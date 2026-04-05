**Example 1: UpdateMCPServerConfig**



Input: 

```
tccli wedata UpdateMCPServerConfig --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --ServerKey 80d2ab301774938861180afb429e8 \
    --Description description \
    --ServerName 测试更新
```

Output: 
```
{
    "Response": {
        "Data": {
            "ConfigData": "{\"mcpServers\": {\"km\": {\"url\": \"https://prod.mcp.it.woa.com/paasfront_km-pro_woa_com/mcp\", \"headers\": {\"Authorization\": \"Bearer tai_pat_WIcaDZY5EqghPfvUN3NHHEFtCereaL6Bbq7f17FqcWU.42Y_vXa7gr_JL8Hkg-XegLOpkAO0SU5gPEuw07OIrAU\"}}}}",
            "CreatedBy": "700002164619",
            "CreatedOn": "1774938861183",
            "Description": "description",
            "Key": "80d2ab301774938861180afb429e8",
            "ModifiedBy": "700002164619",
            "ModifiedOn": "1774962079926",
            "RefResource": "",
            "ServerName": "测试更新",
            "ServerType": "external",
            "ServerUrl": "https://mcp-test001.wedataapp-test.cloud.tencent.com/api/1.0/mcp/http/external/80d2ab301774938861180afb429e8",
            "Status": "active",
            "TransportType": "streamable-http",
            "WorkspaceId": "17678671667189298"
        },
        "RequestId": "45164821-92d4-422d-ad42-aa84036feb51"
    }
}
```

