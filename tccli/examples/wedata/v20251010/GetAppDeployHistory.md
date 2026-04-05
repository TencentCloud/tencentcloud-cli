**Example 1: 部署历史**



Input: 

```
tccli wedata GetAppDeployHistory --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --DeployKey 97137a8a1774421371472fbbcb38e
```

Output: 
```
{
    "Response": {
        "Data": {
            "DeployKey": "97137a8a1774421371472fbbcb38e",
            "Status": "SUCCESS",
            "Steps": [
                {
                    "Description": "部署开始, appKey=627090341774421301601cd964c4a, versionNumber=v1",
                    "Flag": "SUCCESS",
                    "Time": "2026-03-25 06:49:31.470"
                }
            ]
        },
        "RequestId": "336b18c1-58e6-4631-9002-ca8cd88461c1"
    }
}
```

