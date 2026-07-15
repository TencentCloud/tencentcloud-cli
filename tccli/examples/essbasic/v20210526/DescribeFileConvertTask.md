**Example 1: 查询任务状态示例**

查询任务状态示例

Input: 

```
tccli essbasic DescribeFileConvertTask --cli-unfold-argument  \
    --TaskId 2026070*******875611 \
    --Agent.AppId yDwf2UUckps***********0CI2wZ3T8l \
    --Agent.ProxyOrganizationOpenId eddison******org_id \
    --Agent.ProxyOperator.OpenId eddi****hen
```

Output: 
```
{
    "Response": {
        "ResourceId": "yD3JjUUckpe***********SyKZOd5IdY",
        "TaskId": "2026070*******875611",
        "TaskMessage": "任务处理完成",
        "TaskStatus": 8,
        "RequestId": "1ba4d7f8-b9a1-453a-9b5b-254ec5de5ded"
    }
}
```

