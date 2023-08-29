**Example 1: 服务重启**

服务重启

Input: 

```
tccli tem RestartApplication --cli-unfold-argument  \
    --ApplicationId abc \
    --SourceChannel 0 \
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

