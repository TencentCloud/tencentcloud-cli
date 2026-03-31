**Example 1: 获取离线接入任务列表**



Input: 

```
tccli wedata ListIntegrationTasks --cli-unfold-argument  \
    --WorkspaceId 17678671667111111 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskInfoSet": [
                {
                    "Id": "a57fdcce-c2ae-419a-bc69-8de6e8eb45da",
                    "TaskId": "6631fba6-b43d-463c-b4d7-d7a02a6f938c",
                    "TaskName": "file_system_success_20260205_165751",
                    "TaskMode": "1",
                    "SyncType": "0",
                    "UserUinInCharge": "700002161111",
                    "ResourceGroupId": "res-00b25e3a",
                    "Description": "",
                    "InputConnectionType": "FILE_SYSTEM",
                    "OutputConnectionType": "",
                    "InputConnectionIds": [],
                    "OutputConnectionIds": [],
                    "InputDbNames": [],
                    "OutputDbNames": [],
                    "InputTbNames": [],
                    "OutputTbNames": [],
                    "CosPath": "",
                    "TaskVersion": "",
                    "IsProd": "0",
                    "PublishedVersion": "",
                    "Published": false,
                    "Nodes": [],
                    "Mappings": [],
                    "Config": [],
                    "ExtConfig": [],
                    "ExecuteContext": [],
                    "WorkspaceId": "17678671667111111",
                    "OwnerUin": "700002164619",
                    "CreatorUin": "700002164619",
                    "UpdaterUin": "700002164619",
                    "CreateTime": "1770281785641",
                    "UpdateTime": "1770281785641",
                    "AppId": "260071111",
                    "Permission": "MANAGE",
                    "UserUinInChargeName": "wedata-test-User",
                    "CreatorName": "wedata-test-User",
                    "UpdaterName": "wedata-test-User",
                    "PublishedTime": ""
                }
            ],
            "TotalCount": "10"
        },
        "RequestId": "712e6d17-38b2-4b88-95cb-9c5bc0a04e08"
    }
}
```

