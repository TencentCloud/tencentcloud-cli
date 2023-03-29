**Example 1: 编辑Datahub连接源**

编辑Datahub连接源

Input: 

```
tccli ckafka ModifyConnectResource --cli-unfold-argument  \
    --Description xxx \
    --DtsConnectParam.UserName xxx \
    --DtsConnectParam.Resource xxx \
    --DtsConnectParam.GroupId xxx \
    --DtsConnectParam.Password xxx \
    --DtsConnectParam.Topic xxx \
    --DtsConnectParam.Port 0 \
    --ResourceName xxx \
    --ResourceId reource-xxx \
    --Type DTS
```

Output: 
```
{
    "Response": {
        "Result": {
            "ResourceId": "resource-xx"
        },
        "RequestId": "xxx"
    }
}
```

