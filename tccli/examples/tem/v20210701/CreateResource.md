**Example 1: 绑定云资源**

绑定云资源

Input: 

```
tccli tem CreateResource --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --ResourceType CFS \
    --ResourceId resource-xxxxxx \
    --SourceChannel 0 \
    --ResourceFrom existing
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

