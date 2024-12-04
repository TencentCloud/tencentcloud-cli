**Example 1: 编辑Datahub连接源**

编辑Datahub连接源

Input: 

```
tccli ckafka ModifyConnectResource --cli-unfold-argument  \
    --Description yourdescription \
    --DtsConnectParam.UserName user \
    --DtsConnectParam.Resource resource \
    --DtsConnectParam.GroupId groupid \
    --DtsConnectParam.Password yourpassword \
    --DtsConnectParam.Topic topic-test \
    --DtsConnectParam.Port 0 \
    --ResourceName resource-name \
    --ResourceId reource-test \
    --Type DTS
```

Output: 
```
{
    "Response": {
        "Result": {
            "ResourceId": "resource-test"
        },
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
    }
}
```

