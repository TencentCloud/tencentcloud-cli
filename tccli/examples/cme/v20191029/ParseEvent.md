**Example 1: 分析分类创建事件内容**

  

Input: 

```
tccli cme ParseEvent --cli-unfold-argument  \
    --Platform test \
    --EventContent {"EventType":"Class.Created","Operator":"3fa6b09e-05c6-433e-bc1e-6457d290d9d9","MaterialImportedEvent":{"Owner":{"Id":"user_9949009d9d9","Type":"PERSON"},"ClassPath":"/媒体"}}
```

Output: 
```
{
    "Response": {
        "EventContent": {
            "EventType": "Class.Created",
            "Operator": "3fa6b09e-05c6-433e-bc1e-6457d290d9d9",
            "ClassCreatedEvent": {
                "Owner": {
                    "Id": "user_9949009d9d9",
                    "Type": "PERSON"
                },
                "ClassPath": "/媒体"
            },
            "ProjectStreamConnectStatusChangedEvent": {
                "ProjectId": "",
                "Status": "",
                "InputInterruptInfo": null,
                "OutputInterruptInfo": null
            },
            "StorageNewFileCreatedEvent": {
                "FileId": "",
                "MaterialId": "",
                "Operator": "",
                "OperationType": "",
                "Owner": {
                    "Type": "",
                    "Id": ""
                },
                "ClassPath": "",
                "TaskId": "",
                "SourceContext": ""
            },
            "ProjectSwitcherStatusChangedEvent": null,
            "MaterialImportedEvent": null,
            "MaterialAddedEvent": null,
            "MaterialMovedEvent": null,
            "MaterialModifiedEvent": null,
            "MaterialDeletedEvent": null,
            "ClassMovedEvent": null,
            "ClassDeletedEvent": null,
            "VideoExportCompletedEvent": null,
            "ProjectMediaCastStatusChangedEvent": null
        },
        "RequestId": "946c2480-a14f-4d18-8a09-31a45cbd21af"
    }
}
```

**Example 2: 分析媒体导入事件内容**

 

Input: 

```
tccli cme ParseEvent --cli-unfold-argument  \
    --Platform test \
    --EventContent {"EventType":"Material.Imported","Operator":"3fa6b09e-05c6-433e-bc1e-6457d290d9d9","MaterialImportedEvent":{"MediaInfoSet":["9dd28590d08987ujd795d","rdd28590d08187ujd7095d"],"Owner":{"Id":"user_9949009d9d9","Type":"PERSON"},"ClassPath":"/媒体"}}
```

Output: 
```
{
    "Response": {
        "EventContent": {
            "EventType": "Material.Imported",
            "Operator": "3fa6b09e-05c6-433e-bc1e-6457d290d9d9",
            "MaterialImportedEvent": {
                "MediaInfoSet": [
                    {
                        "MaterialId": "9dd28590d08987ujd795d"
                    },
                    {
                        "MaterialId": "rdd28590d08187ujd7095d"
                    }
                ],
                "Owner": {
                    "Id": "user_9949009d9d9",
                    "Type": "PERSON"
                },
                "ClassPath": "/媒体"
            },
            "ProjectStreamConnectStatusChangedEvent": {
                "ProjectId": "",
                "Status": "",
                "InputInterruptInfo": null,
                "OutputInterruptInfo": null
            },
            "StorageNewFileCreatedEvent": {
                "FileId": "",
                "MaterialId": "",
                "Operator": "",
                "OperationType": "",
                "Owner": {
                    "Type": "",
                    "Id": ""
                },
                "ClassPath": "",
                "TaskId": "",
                "SourceContext": ""
            },
            "ProjectSwitcherStatusChangedEvent": null,
            "MaterialAddedEvent": null,
            "MaterialMovedEvent": null,
            "MaterialModifiedEvent": null,
            "MaterialDeletedEvent": null,
            "ClassCreatedEvent": null,
            "ClassMovedEvent": null,
            "ClassDeletedEvent": null,
            "VideoExportCompletedEvent": null,
            "ProjectMediaCastStatusChangedEvent": null
        },
        "RequestId": "946c2480-a14f-4d18-8a09-31a45cbd21af"
    }
}
```

**Example 3: 分析新文件产生事件内容**

 

Input: 

```
tccli cme ParseEvent --cli-unfold-argument  \
    --Platform test \
    --EventContent {"EventType":"Storage.NewFileCreated","Operator":"3fa6b09e-05c6-433e-bc1e-6457d290d9d9","StorageNewFileCreatedEvent":{"FileId":"5285890818667693851","MaterialId":"60a75c1c30fcbe0001cc09d5","Operator":"3fa6b09e-05c6-433e-bc1e-6457d264f1dd","OperationType":"Upload","Owner":{"Type":"PERSON","Id":"3fa6b09e-05c6-433e-bc1e-6457d264f1dd"},"ClassPath":"/媒体"}}
```

Output: 
```
{
    "Response": {
        "EventContent": {
            "EventType": "Storage.NewFileCreated",
            "Operator": "3fa6b09e-05c6-433e-bc1e-6457d290d9d9",
            "StorageNewFileCreatedEvent": {
                "FileId": "85890818667698972737",
                "MaterialId": "60a75c1c30fcbe00093ikd93k",
                "Operator": "3fa6b09e-05c6-433e-bc1e-6457d290d9d9",
                "OperationType": "Upload",
                "Owner": {
                    "Type": "PERSON",
                    "Id": "3fa6b09e-05c6-433e-bc1e-6457d290d9d9"
                },
                "ClassPath": "/媒体",
                "TaskId": "",
                "SourceContext": ""
            },
            "ProjectStreamConnectStatusChangedEvent": {
                "ProjectId": "",
                "Status": "",
                "InputInterruptInfo": null,
                "OutputInterruptInfo": null
            },
            "ProjectSwitcherStatusChangedEvent": null,
            "MaterialImportedEvent": null,
            "MaterialAddedEvent": null,
            "MaterialMovedEvent": null,
            "MaterialModifiedEvent": null,
            "MaterialDeletedEvent": null,
            "ClassCreatedEvent": null,
            "ClassMovedEvent": null,
            "ClassDeletedEvent": null,
            "VideoExportCompletedEvent": null,
            "ProjectMediaCastStatusChangedEvent": null
        },
        "RequestId": "946c2480-a14f-4d18-8a09-31a45cbd21af"
    }
}
```

**Example 4: 分析云转推项目状态变更事件内容**

 

Input: 

```
tccli cme ParseEvent --cli-unfold-argument  \
    --Platform test \
    --EventContent {"EventType":"Project.StreamConnect.StatusChanged","Operator":"3fa6b09e-05c6-433e-bc1e-6457d290d9d9","ProjectStreamConnectStatusChangedEvent":{"ProjectId":"5285890818667693851","Status":"Working"}}
```

Output: 
```
{
    "Response": {
        "EventContent": {
            "EventType": "Project.StreamConnect.StatusChanged",
            "Operator": "3fa6b09e-05c6-433e-bc1e-6457d290d9d9",
            "ProjectStreamConnectStatusChangedEvent": {
                "ProjectId": "5285890818667693851",
                "Status": "Working",
                "InputInterruptInfo": null,
                "OutputInterruptInfo": null
            },
            "StorageNewFileCreatedEvent": {
                "FileId": "",
                "MaterialId": "",
                "Operator": "",
                "OperationType": "",
                "Owner": {
                    "Type": "",
                    "Id": ""
                },
                "ClassPath": "",
                "TaskId": "",
                "SourceContext": ""
            },
            "ProjectSwitcherStatusChangedEvent": null,
            "MaterialImportedEvent": null,
            "MaterialAddedEvent": null,
            "MaterialMovedEvent": null,
            "MaterialModifiedEvent": null,
            "MaterialDeletedEvent": null,
            "ClassCreatedEvent": null,
            "ClassMovedEvent": null,
            "ClassDeletedEvent": null,
            "VideoExportCompletedEvent": null,
            "ProjectMediaCastStatusChangedEvent": null
        },
        "RequestId": "946c2480-a14f-4d18-8a09-31a45cbd21af"
    }
}
```

**Example 5: 分析导播台项目状态变更事件内容**

 

Input: 

```
tccli cme ParseEvent --cli-unfold-argument  \
    --Platform test \
    --EventContent {"EventType":"Project.Switcher.StatusChanged","Operator":"3fa6b09e-05c6-433e-bc1e-6457d290d9d9","ProjectSwitcherStatusChangedEvent":{"ProjectId":"add28590d08187ujd7695d","Status":"Started"}}
```

Output: 
```
{
    "Response": {
        "EventContent": {
            "EventType": "Project.Switcher.StatusChanged",
            "Operator": "3fa6b09e-05c6-433e-bc1e-6457d290d9d9",
            "ProjectSwitcherStatusChangedEvent": {
                "ProjectId": "add28590d08187ujd7695d",
                "Status": "Started"
            },
            "ProjectStreamConnectStatusChangedEvent": {
                "ProjectId": "",
                "Status": "",
                "InputInterruptInfo": null,
                "OutputInterruptInfo": null
            },
            "StorageNewFileCreatedEvent": {
                "FileId": "",
                "MaterialId": "",
                "Operator": "",
                "OperationType": "",
                "Owner": {
                    "Type": "",
                    "Id": ""
                },
                "ClassPath": "",
                "TaskId": "",
                "SourceContext": ""
            },
            "MaterialImportedEvent": null,
            "MaterialAddedEvent": null,
            "MaterialMovedEvent": null,
            "MaterialModifiedEvent": null,
            "MaterialDeletedEvent": null,
            "ClassCreatedEvent": null,
            "ClassMovedEvent": null,
            "ClassDeletedEvent": null,
            "VideoExportCompletedEvent": null,
            "ProjectMediaCastStatusChangedEvent": null
        },
        "RequestId": "946c2480-a14f-4d18-8a09-31a45cbd21af"
    }
}
```

