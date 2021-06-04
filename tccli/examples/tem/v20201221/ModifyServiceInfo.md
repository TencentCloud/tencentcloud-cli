**Example 1: 修改服务基本信息**

修改服务基本信息

Input: 

```
tccli tem ModifyServiceInfo --cli-unfold-argument  \
    --Description xx \
    --SourceChannel 0 \
    --ServiceId xx
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

