**Example 1: 开始下一批次发布**



Input: 

```
tccli tem ResumeDeployApplication --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --EnvironmentId en-xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx-xxx-xxx"
    }
}
```

