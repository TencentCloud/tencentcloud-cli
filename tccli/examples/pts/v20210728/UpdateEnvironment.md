**Example 1: 更新环境**

更新环境

Input: 

```
tccli pts UpdateEnvironment --cli-unfold-argument  \
    --ProjectId project-xx \
    --EnvId env-xx \
    --Name abc \
    --Description abc \
    --EnvVars.0.Name abc \
    --EnvVars.0.Value abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

