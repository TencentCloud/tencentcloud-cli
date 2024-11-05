**Example 1: 修改应用基本信息**

修改应用基本信息

Input: 

```
tccli tem ModifyApplicationInfo --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId app-xxxxxx \
    --Description test \
    --EnableTracing 1
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "true"
    }
}
```

