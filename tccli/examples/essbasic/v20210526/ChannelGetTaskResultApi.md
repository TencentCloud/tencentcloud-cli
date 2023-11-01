**Example 1: 查询转换任务**

查询文件转换任务

Input: 

```
tccli essbasic ChannelGetTaskResultApi --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --TaskId yDRS4UUgygqdcj56UuO4zjExBQcOiB68
```

Output: 
```
{
    "Response": {
        "RequestId": "s1698837600515440954",
        "ResourceId": "yDSLOUUckpoji469U5GRz2w1NRiV2lPp",
        "TaskId": "20231101191954296703",
        "TaskMessage": "任务处理完成",
        "TaskStatus": 8
    }
}
```

