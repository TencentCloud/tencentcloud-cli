**Example 1: 异步重试配置请求示例**



Input: 

```
tccli scf UpdateFunctionEventInvokeConfig --cli-unfold-argument  \
    --FunctionName FunctionName \
    --Namespace default \
    --AsyncTriggerConfig.MsgTTL 3600 \
    --AsyncTriggerConfig.RetryConfig.0.RetryNum 1
```

Output: 
```
{
    "Response": {
        "RequestId": "XXXXXX"
    }
}
```

