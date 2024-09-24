**Example 1: 示例**

示例

Input: 

```
tccli mqtt UpdateAuthorizationPolicyPriority --cli-unfold-argument  \
    --InstanceId mqtt-g4r4x85z \
    --Priorities.0.Id 1 \
    --Priorities.0.Priority 3 \
    --Priorities.1.Id 6 \
    --Priorities.1.Priority 1 \
    --Priorities.2.Id 7 \
    --Priorities.2.Priority 2
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "1186da0d-931d-47a3-80a1-885ea2c00067"
    }
}
```

