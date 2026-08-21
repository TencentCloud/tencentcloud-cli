**Example 1: 按 COS URI 删除 TWeSee 视觉理解任务**

精确匹配任务来源 COS URI，删除对应的视觉理解任务。

Input: 

```
tccli iotexplorer DeleteTWeSeeTasksByCondition --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ChannelId 0 \
    --ServiceCategory COMPREHENSION \
    --Conditions.0.Type COSURI \
    --Conditions.0.Values cos://bucket.ap-guangzhou/Direct/10001/session-id/video.mp4
```

Output: 
```
{
    "Response": {
        "RequestId": "5e24e488-7948-4ff6-9bd1-76eb3a0cd112"
    }
}
```

**Example 2: 按 COS URI 前缀删除 TWeSee 视觉理解任务**

匹配指定 COS URI 前缀，删除该前缀下的视觉理解任务。

Input: 

```
tccli iotexplorer DeleteTWeSeeTasksByCondition --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ChannelId 0 \
    --ServiceCategory COMPREHENSION \
    --Conditions.0.Type COSURIPrefix \
    --Conditions.0.Values cos://bucket.ap-guangzhou/Direct/10001/session-id/
```

Output: 
```
{
    "Response": {
        "RequestId": "069dc8b7-2d75-4377-8907-6c99ceba8b92"
    }
}
```

**Example 3: 按任务 ID 删除 TWeSee 视觉理解任务**

删除指定任务 ID 对应的视觉理解任务。

Input: 

```
tccli iotexplorer DeleteTWeSeeTasksByCondition --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ChannelId 0 \
    --ServiceCategory COMPREHENSION \
    --Conditions.0.Type TaskId \
    --Conditions.0.Values comp-d57939bb-b155-5623-c7e7-1fb8dd0654dd
```

Output: 
```
{
    "Response": {
        "RequestId": "ecdb8ebc-b257-43f0-af93-105b0cfa94c0"
    }
}
```

**Example 4: 按时间范围删除 TWeSee 视觉理解任务**

删除任务时间范围与指定时间范围有重合的视觉理解任务。

Input: 

```
tccli iotexplorer DeleteTWeSeeTasksByCondition --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ChannelId 0 \
    --ServiceCategory COMPREHENSION \
    --Conditions.0.Type TimeRange \
    --Conditions.0.Values 1776621600,1776636000
```

Output: 
```
{
    "Response": {
        "RequestId": "93651c85-82f1-4214-befa-e737777852eb"
    }
}
```

