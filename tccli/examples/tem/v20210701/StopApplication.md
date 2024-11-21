**Example 1: 服务版本停止**

服务版本停止

Input: 

```
tccli tem StopApplication --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId app-xxxxxx \
    --EnvironmentId en-xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc-xxxx-xxxx"
    }
}
```

