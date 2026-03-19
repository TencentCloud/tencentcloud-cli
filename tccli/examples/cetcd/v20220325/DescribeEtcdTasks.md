**Example 1: 查看etcd相关tasks**



Input: 

```
tccli cetcd DescribeEtcdTasks --cli-unfold-argument  \
    --Filters.0.Name taskType \
    --Filters.0.Values enable_internet disable_internet \
    --Filters.1.Name resourceId \
    --Filters.1.Values etcd-xxxx \
    --Filters.2.Name lifeState \
    --Filters.2.Values process
```

Output: 
```
{
    "Response": {
        "RequestId": "49035d1e-66c6-4ee5-a74f-21d869fccab9",
        "Tasks": [
            {
                "CreatedAt": "2021-09-01T10:43:29Z",
                "LifeState": "done",
                "ResourceID": "etcd-jirlfihs",
                "TaskID": "4fee3bfe-7670-4014-82d4-31507e3a93f4",
                "TaskType": "enable_internet",
                "UpdatedAt": "2021-09-01T10:43:40Z"
            },
            {
                "CreatedAt": "2021-08-26T03:04:06Z",
                "LifeState": "done",
                "ResourceID": "etcd-jirlfihs",
                "TaskID": "a59278a0-debb-4e85-861b-961a2d2f0f46",
                "TaskType": "create_instance",
                "UpdatedAt": "2021-08-26T03:07:09Z"
            }
        ]
    }
}
```

