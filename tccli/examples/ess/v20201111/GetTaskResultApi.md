**Example 1: test示例**



Input: 

```
tccli ess GetTaskResultApi --cli-unfold-argument  \
    --Operator.ProxyIp  \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.UserId yDxoQUUgydjfn4yaUuO4zjEyd1h2hnnR \
    --Operator.Channel  \
    --Operator.OpenId  \
    --Organization.OrganizationOpenId  \
    --Organization.OrganizationId 682c1d5bdce884ad3df5ba5fabb6fcf1 \
    --Organization.ClientIp  \
    --Organization.ProxyIp  \
    --Organization.Channel  \
    --TaskId 20220726183047992850
```

Output: 
```
{
    "Response": {
        "RequestId": "2255ca9d-d831-4c9d-ab76-6192fc301053",
        "ResourceId": "yDRtsUUgygq7jtzwUuO4zjEyx4jZM3A7",
        "TaskId": "20220726183047992850",
        "TaskMessage": "任务处理完成",
        "TaskStatus": 8
    }
}
```

