**Example 1: 修改版本规格**

修改版本规格

Input: 

```
tccli tem ModifyApplicationReplicas --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx \
    --Replicas 0
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

