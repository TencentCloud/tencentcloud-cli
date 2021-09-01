**Example 1: 批量导入API至api分组**



Input: 

```
tccli tsf CreateGatewayApi --cli-unfold-argument  \
    --GroupId grp-5yk7oor1 \
    --ApiList.0.NamespaceId ns-do1n280j \
    --ApiList.0.MicroserviceId ms-sf26d1gf1 \
    --ApiList.0.Path /user/find \
    --ApiList.0.Method POST \
    --ApiList.0.PathMapping /user/find
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e5507e42d5970cd2e25ed5267a",
        "Result": true
    }
}
```

