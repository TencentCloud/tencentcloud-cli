**Example 1: 查询部署结果**



Input: 

```
tccli wedata ListAppDeploys --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --AppKey 330dd6f5177432457674675f5d116 \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 11 \
    --PageRequest.AllPage True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AppKey": "330dd6f5177432457674675f5d116",
                    "CreatedBy": "700002164618",
                    "CreatedOn": "1774325196201",
                    "DeployLog": "部署失败: ConnectRPC 流式调用异常 [process.Process/Start]",
                    "Duration": "910",
                    "FinishedOn": "1774325196847",
                    "Key": "abe4f55b177432519620289c794dd",
                    "Status": "FAILED",
                    "TriggeredBy": "MANUAL",
                    "VersionKey": "2a14a3b0177432519618659421aeb",
                    "VersionNumber": "v4"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 11,
                "TotalCount": 4,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "40bc4dcf-ab26-45fc-8cf6-f6faa8bfaaa3"
    }
}
```

