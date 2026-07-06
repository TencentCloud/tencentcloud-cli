**Example 1: 创建转换任务示例**

创建转换任务示例

Input: 

```
tccli essbasic CreateFileConvertTask --cli-unfold-argument  \
    --Agent.AppId yDwf2UUckps***********0CI2wZ3T8l \
    --Agent.ProxyOrganizationOpenId eddison******org_id \
    --Agent.ProxyOperator.OpenId eddi****hen \
    --ResourceType docx \
    --ResourceName 转换 \
    --ResourceId yD3JjUUckpe***********BvOXIhzJjy
```

Output: 
```
{
    "Response": {
        "TaskId": "2026070*******875611",
        "RequestId": "b38f53e0-4893-4ff1-b6c7-57275af8af5f"
    }
}
```

