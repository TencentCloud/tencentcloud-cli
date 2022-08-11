**Example 1: test示例**



Input: 

```
tccli essbasic ChannelGetTaskResultApi --cli-unfold-argument  \
    --Operator.OpenId test1_clara_test1 \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.ProxyIp  \
    --Agent.ProxyOrganizationOpenId test1_clara_open_organization1 \
    --Agent.AppId 7f349*********984a9657b0ec \
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
        "TaskStatus": 8
    }
}
```

