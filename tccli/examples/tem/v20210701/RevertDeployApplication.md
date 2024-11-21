**Example 1: 回滚分批发布**



Input: 

```
tccli tem RevertDeployApplication --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --EnvironmentId en-xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc-xxx-xxxx"
    }
}
```

