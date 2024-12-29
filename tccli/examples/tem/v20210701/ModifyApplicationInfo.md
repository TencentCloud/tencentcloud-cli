**Example 1: 修改应用基本信息**

修改应用基本信息

Input: 

```
tccli tem ModifyApplicationInfo --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId app-xxxxxx \
    --Description 这是一个描述 \
    --EnableTracing 1
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "1dew34d-xxx-xxx-xxx"
    }
}
```

