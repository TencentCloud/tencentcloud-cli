**Example 1: 修改应用基本信息**

修改应用基本信息

Input: 

```
tccli tem ModifyApplicationInfo --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId xx \
    --Description xx \
    --EnableTracing 1
```

Output: 
```
{
    "Response": {
        "Result": "xx",
        "RequestId": "true"
    }
}
```

