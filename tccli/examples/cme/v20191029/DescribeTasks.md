**Example 1: 分页获取视频导出任务列表**

 

Input: 

```
tccli cme DescribeTasks --cli-unfold-argument  \
    --Platform test \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TaskBaseInfoSet": [
            {
                "CreateTime": "2020-04-30T03:26:37Z",
                "ErrCode": 0,
                "ErrMsg": "SUCCESS",
                "Progress": 100,
                "Status": "SUCCESS",
                "TaskId": "181xxxxxxxx9-procedurev2-b718fcee09a72470bf665cf55351d810t0",
                "TaskType": "VIDEO_EDIT_PROJECT_EXPORT"
            }
        ],
        "RequestId": "efde1a47-f1c9-4c1b-911c-9865a6a4d1ac"
    }
}
```

**Example 2: 指定项目 Id 获取视频导出任务列表**

 

Input: 

```
tccli cme DescribeTasks --cli-unfold-argument  \
    --Platform test \
    --Offset 0 \
    --ProjectId cmepid_5fd8ad3d628dc30001bd0895 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TaskBaseInfoSet": [
            {
                "CreateTime": "2020-04-30T03:26:37Z",
                "ErrCode": 0,
                "ErrMsg": "SUCCESS",
                "Progress": 100,
                "Status": "SUCCESS",
                "TaskId": "181xxxxxxxx9-procedurev2-b718fcee09a72470bf665cf55351d810t0",
                "TaskType": "VIDEO_EDIT_PROJECT_EXPORT"
            }
        ],
        "RequestId": "efde1a47-f1c9-4c1b-911c-9865a6a4d1ad"
    }
}
```

**Example 3: 指定任务状态获取视频导出任务列表**

 

Input: 

```
tccli cme DescribeTasks --cli-unfold-argument  \
    --Platform test \
    --StatusSet SUCCESS \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TaskBaseInfoSet": [
            {
                "CreateTime": "2020-04-30T03:26:37Z",
                "ErrCode": 0,
                "ErrMsg": "SUCCESS",
                "Progress": 100,
                "Status": "SUCCESS",
                "TaskId": "181xxxxxxxx9-procedurev2-b718fcee09a72470bf665cf55351d810t0",
                "TaskType": "VIDEO_EDIT_PROJECT_EXPORT"
            }
        ],
        "RequestId": "efde1a47-f1c9-4c1b-911c-9865a6a4d1ae"
    }
}
```

**Example 4: 指定任务类型获取视频导出任务列表**

 

Input: 

```
tccli cme DescribeTasks --cli-unfold-argument  \
    --Platform test \
    --TaskTypeSet VIDEO_EDIT_PROJECT_EXPORT \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TaskBaseInfoSet": [
            {
                "CreateTime": "2020-04-30T03:26:37Z",
                "ErrCode": 0,
                "ErrMsg": "SUCCESS",
                "Progress": 100,
                "Status": "SUCCESS",
                "TaskId": "181xxxxxxxx9-procedurev2-b718fcee09a72470bf665cf55351d810t0",
                "TaskType": "VIDEO_EDIT_PROJECT_EXPORT"
            }
        ],
        "RequestId": "efde1a47-f1c9-4c1b-911c-9865a6a4d133"
    }
}
```

