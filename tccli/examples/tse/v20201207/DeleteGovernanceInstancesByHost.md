**Example 1: 根据HOST删除治理中心某个服务下的实例**

根据HOST删除治理中心某个服务下的实例

Input: 

```
tccli tse DeleteGovernanceInstancesByHost --cli-unfold-argument  \
    --InstanceId abc \
    --GovernanceInstances.0.Service abc \
    --GovernanceInstances.0.Namespace abc \
    --GovernanceInstances.0.Host abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

