**Example 1: 服务重启**

服务重启

Input: 

```
tccli tem RestartApplication --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc-xxx-xxx"
    }
}
```

