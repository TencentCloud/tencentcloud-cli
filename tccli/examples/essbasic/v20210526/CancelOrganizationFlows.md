**Example 1: 全量撤销企业合同**

全量撤销企业合同

Input: 

```
tccli essbasic CancelOrganizationFlows --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId es******************n_1 \
    --Agent.ProxyOperator.OpenId k*********g
```

Output: 
```
{
    "Response": {
        "TaskId": "yD3PzUUckpzfafu8UaytqwM63aaNhNqP",
        "RequestId": "658033fa-247c-4e49-b8e5-cc7da03b1863"
    }
}
```

