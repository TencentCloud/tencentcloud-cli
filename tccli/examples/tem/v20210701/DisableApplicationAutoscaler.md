**Example 1: 修改版本规格**

修改版本规格

Input: 

```
tccli tem DisableApplicationAutoscaler --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId xx \
    --EnvironmentId xx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx"
    }
}
```

