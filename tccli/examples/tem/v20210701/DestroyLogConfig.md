**Example 1: 销毁日志收集配置**

销毁日志收集配置

Input: 

```
tccli tem DestroyLogConfig --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --Name name-xxx \
    --ApplicationId app-xxxxxx
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

