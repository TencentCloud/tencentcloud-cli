**Example 1: 用于修改服务**

用于修改服务的相关信息。

Input: 

```
tccli apigateway ModifyService --cli-unfold-argument  \
    --ServiceId service-0c96l2bo \
    --ServiceName test_https \
    --ServiceDesc https \
    --Protocol https
```

Output: 
```
{
    "Response": {
        "RequestId": "e3705d00-bfe0-4fde-942c-cebd6b12431b"
    }
}
```

