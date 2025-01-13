**Example 1: 更新环境**

更新环境

Input: 

```
tccli pts UpdateEnvironment --cli-unfold-argument  \
    --ProjectId project-1a2b3c4d \
    --EnvId env-1a2b3c4d \
    --Name name \
    --Description test env \
    --EnvVars.0.Name name1 \
    --EnvVars.0.Value value1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-123-xyz"
    }
}
```

