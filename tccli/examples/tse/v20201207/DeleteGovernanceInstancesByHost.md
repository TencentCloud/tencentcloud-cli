**Example 1: 根据HOST删除治理中心某个服务下的实例**

根据HOST删除治理中心某个服务下的实例

Input: 

```
tccli tse DeleteGovernanceInstancesByHost --cli-unfold-argument  \
    --InstanceId ins-id \
    --GovernanceInstances.0.Service service \
    --GovernanceInstances.0.Namespace namespace \
    --GovernanceInstances.0.Host 127.0.0.1
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "req-id"
    }
}
```

