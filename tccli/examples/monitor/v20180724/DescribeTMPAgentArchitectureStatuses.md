**Example 1: 仅传入实例InstanceId**

仅传入实例InstanceId，返回所有相关tmp-agent架构状态

Input: 

```
tccli monitor DescribeTMPAgentArchitectureStatuses --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "f5c04cb5-869d-7426-78b8-e978c01875b1"
    }
}
```

**Example 2: 传入实例InstacneId和集群ClusterId**

传入实例InstacneId和集群ClusterId，返回相关tmp-agent架构状态

Input: 

```
tccli monitor DescribeTMPAgentArchitectureStatuses --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "f5c04cb5-869d-7426-78b8-e978c01875b1"
    }
}
```

