**Example 1: 查询转换任务**

查询文件转换任务

Input: 

```
tccli essbasic ChannelGetTaskResultApi --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId yDxAyUyK****cb7u0jQn0Zh7f7 \
    --Agent.ProxyOperator.OpenId 732aaef****541b89c49e0cc \
    --Agent.AppId ed68bc6***********0214e4e \
    --TaskId 2022*********589282
```

Output: 
```
{
    "Response": {
        "RequestId": "3f08b529-f13e-4129-85a4-9585fd794656",
        "ResourceId": "yDRt2*********EytoAXw44x",
        "TaskId": "2022*********4589282",
        "TaskMessage": "任务处理完成",
        "TaskStatus": 8,
        "PreviewUrl": ""
    }
}
```

