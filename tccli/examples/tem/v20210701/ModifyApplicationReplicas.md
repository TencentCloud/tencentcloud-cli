**Example 1: 修改版本规格**

修改版本规格

Input: 

```
tccli tem ModifyApplicationReplicas --cli-unfold-argument  \
    --ApplicationId abc \
    --SourceChannel 0 \
    --EnvironmentId abc \
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

