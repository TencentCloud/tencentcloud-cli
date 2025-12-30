**Example 1: 创建环境**

创建环境

Input: 

```
tccli pts CreateEnvironment --cli-unfold-argument  \
    --ProjectId project-1a2b3c4d \
    --Name env-name \
    --Description env-description \
    --EnvVars.0.Name name-1 \
    --EnvVars.0.Value value-1
```

Output: 
```
{
    "Response": {
        "EnvId": "env-1a2b3c4d",
        "RequestId": "abc-123-xyz"
    }
}
```

