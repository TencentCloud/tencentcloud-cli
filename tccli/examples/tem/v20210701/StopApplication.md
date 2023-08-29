**Example 1: 服务版本停止**

服务版本停止

Input: 

```
tccli tem StopApplication --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId abc \
    --EnvironmentId abc
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

