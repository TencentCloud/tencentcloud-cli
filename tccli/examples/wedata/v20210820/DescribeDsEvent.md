**Example 1: 分页查询事件**

分页查询事件

Input: 

```
tccli wedata DescribeDsEvent --cli-unfold-argument  \
    --ProjectId abc \
    --EventName abc \
    --EventType abc \
    --EventSubType abc \
    --DatetimeFormat abc \
    --CreationTimeStart abc \
    --CreationTimeEnd abc \
    --PageSize 0 \
    --PageNumber 0 \
    --OrderFields.0.Name creationTs \
    --OrderFields.0.Direction DESC
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalItems": 0,
            "TotalPages": 0,
            "CurrentPageItems": 0,
            "CurrentPage": 0,
            "PageSize": 0,
            "Items": [
                {
                    "Name": "abc",
                    "EventType": "abc",
                    "EventSubType": "abc",
                    "EventBroadcastType": "abc",
                    "DimensionFormat": "abc",
                    "TimeToLive": 0,
                    "TimeUnit": "abc",
                    "CreationTs": "abc",
                    "Owner": "abc",
                    "Properties": "abc",
                    "Description": "abc",
                    "Listeners": [
                        {
                            "Key": "abc",
                            "Type": "abc",
                            "CreationTs": "abc",
                            "PropertiesList": [
                                {
                                    "ParamKey": "abc",
                                    "ParamValue": "abc"
                                }
                            ],
                            "EventName": "abc",
                            "TaskInfo": {
                                "TaskId": "abc",
                                "TaskName": "abc",
                                "WorkflowId": "abc",
                                "WorkflowName": "abc",
                                "TaskTypeId": 0,
                                "TaskType": "abc",
                                "ProjectId": "abc"
                            },
                            "EventProjectId": "abc"
                        }
                    ],
                    "ProjectId": "abc",
                    "ProjectName": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 错误示例**

错误示例

Input: 

```
tccli wedata DescribeDsEvent --cli-unfold-argument  \
    --ProjectId 1470561602745229312 \
    --EventName  \
    --EventSubType  \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作"
        },
        "RequestId": "1b79e128-815b-4902-bac3-8d8e72284d56"
    }
}
```

