**Example 1: 批量导入API至api分组**



Input: 

```
tccli tsf CreateGatewayApi --cli-unfold-argument  \
    --GroupId grp-djvzrdih \
    --ApiList.0.NamespaceId namespace-external \
    --ApiList.0.MicroserviceId ms-external \
    --ApiList.0.Path /echo_user \
    --ApiList.0.Method GET \
    --ApiList.0.PathMapping /echo_user \
    --ApiList.0.Host http://www.qq.com \
    --ApiList.0.Description This is desc \
    --ProgramIdList program-6a79x94v
```

Output: 
```
{
    "Response": {
        "RequestId": "e521be92-af1e-4d1c-bcd9-31bfe1ff0859",
        "Result": true
    }
}
```

