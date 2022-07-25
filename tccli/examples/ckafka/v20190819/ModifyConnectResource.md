**Example 1: 编辑Datahub连接源**



Input: 

```
tccli ckafka ModifyConnectResource --cli-unfold-argument  \
    --Description xx \
    --DtsConnectParam.UserName xx \
    --DtsConnectParam.Resource xx \
    --DtsConnectParam.GroupId xx \
    --DtsConnectParam.Password xx \
    --DtsConnectParam.Topic xx \
    --DtsConnectParam.Port 0 \
    --ResourceName xx \
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
        "RequestId": "xx"
    }
}
```

