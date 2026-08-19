**Example 1: 修改路由安全组关联**



Input: 

```
tccli ckafka ModifyRouteSecurityGroups --cli-unfold-argument  \
    --InstanceRoute.InstanceId ckafka-test1234 \
    --InstanceRoute.RouteId 1234 \
    --SecurityGroupIds sg-xxx1 sg-xxx2
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "success"
        },
        "RequestId": "test-reqId-1135"
    }
}
```

