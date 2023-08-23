**Example 1: 创建环境**

创建环境

Input: 

```
tccli pts CreateEnvironment --cli-unfold-argument  \
    --ProjectId project-xx \
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

