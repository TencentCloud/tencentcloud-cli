**Example 1: 服务版本删除**

服务版本删除

Input: 

```
tccli tem DeleteApplication --cli-unfold-argument  \
    --ApplicationId abc \
    --SourceChannel 0 \
    --EnvironmentId abc \
    --DeleteApplicationIfNoRunningVersion True
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": true
    }
}
```

