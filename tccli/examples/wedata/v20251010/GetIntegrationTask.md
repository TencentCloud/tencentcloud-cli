**Example 1: 获取接入任务信息**



Input: 

```
tccli wedata GetIntegrationTask --cli-unfold-argument  \
    --TaskVersion 202512121001 \
    --WorkspaceId 1767867166711118 \
    --TaskId 2f512f8a-109d-4e24-b589-8b2af8ead73c \
    --IsProd 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskInfo": {
                "Id": "7f369000-0c91-4f06-bb7c-359f3244ea5c",
                "TaskId": "2f512f8a-109d-4e24-b589-8b2af8ead73c",
                "TaskName": "MYSQL_20260205_165330",
                "TaskMode": "1",
                "SyncType": "0",
                "UserUinInCharge": "700002164619",
                "ResourceGroupId": "res-00b25e3a",
                "Description": "",
                "InputConnectionType": "MYSQL",
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
                "WorkspaceId": "1767867166711118",
                "OwnerUin": "700002164619",
                "CreatorUin": "700002164619",
                "UpdaterUin": "700002164619",
                "CreateTime": "1770281617817",
                "UpdateTime": "1770281617817",
                "AppId": "260073493",
                "Permission": "MANAGE",
                "UserUinInChargeName": "wedata-test-user",
                "CreatorName": "wedata-test-user",
                "UpdaterName": "wedata-test-user",
                "PublishedTime": ""
            }
        },
        "RequestId": "07bdc058-9fc3-4e0a-bbaa-ccbf7a679f4d"
    }
}
```

