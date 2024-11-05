**Example 1: 删除一条访问方式**



Input: 

```
tccli tem DeleteApplicationService --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx \
    --ServiceName abc-xxx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx-xxx-xxxx"
    }
}
```

