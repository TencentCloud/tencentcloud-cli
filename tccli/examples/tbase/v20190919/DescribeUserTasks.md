**Example 1: 查询任务列表和详情**



Input: 

```
tccli tbase DescribeUserTasks --cli-unfold-argument  \
    --Limit 0 \
    --Filters.0.Values tdpg-oobic9i0 tdpg-oobic9i1 \
    --Filters.0.Name InstanceIds \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "2977eea7ae5012774f1464c1f",
        "TaskList": [
            {
                "Status": "success",
                "InstanceId": "tdpg-oobic9i0",
                "AppId": 12345678,
                "Id": 1,
                "TaskType": "create",
                "Progress": 100,
                "EndTime": "2021-03-20 15:00:00",
                "InstanceName": "tdpg-oobic9i0",
                "CreateTime": "2021-03-20 14:58:00",
                "ErrMsg": ""
            }
        ]
    }
}
```

