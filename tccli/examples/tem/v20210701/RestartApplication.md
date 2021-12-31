**Example 1: 服务版本停止**

服务版本停止

Input: 

```
tccli tem RestartApplication --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId xx \
    --EnvironmentId xx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx"
    }
}
```

