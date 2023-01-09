**Example 1: 调用示例**



Input: 

```
tccli ess CreateConvertTaskApi --cli-unfold-argument  \
    --ResourceType doc \
    --ResourceId y***********************************l \
    --Organization.OrganizationOpenId  \
    --Organization.OrganizationId  \
    --Organization.ClientIp  \
    --Organization.ProxyIp  \
    --Organization.Channel  \
    --Operator.ProxyIp  \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.UserId y***********************************p \
    --Operator.Channel  \
    --Operator.OpenId  \
    --ResourceName hello.docx
```

Output: 
```
{
    "Response": {
        "RequestId": "b2eae803-fe6e-4b1c-8901-c61cfaf19a21",
        "TaskId": "20220726175923011294"
    }
}
```

**Example 2: test示例**



Input: 

```
tccli ess CreateConvertTaskApi --cli-unfold-argument  \
    --ResourceType doc \
    --ResourceName hello.docx \
    --Operator.ProxyIp 8.8.8.8 \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.UserId y***********************************R \
    --Organization.OrganizationId 6***********************************1 \
    --Organization.ClientIp 8.8.8.8 \
    --Organization.ProxyIp 8.8.8.8 \
    --ResourceId y***********************************l
```

Output: 
```
{
    "Response": {
        "RequestId": "fbf25f31-1b45-4ed5-9b45-8afed19e9849",
        "TaskId": "20220728163549202141"
    }
}
```

