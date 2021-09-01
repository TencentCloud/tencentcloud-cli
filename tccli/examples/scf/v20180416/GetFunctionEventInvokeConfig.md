**Example 1: 获取异步配置请求示例**



Input: 

```
tccli scf GetFunctionEventInvokeConfig --cli-unfold-argument  \
    --FunctionName Unzip-1609933864 \
    --Namespace default \
    --Qualifier $LATEST
```

Output: 
```
{
    "Response": {
        "AsyncTriggerConfig": {
            "MsgTTL": 3600,
            "RetryConfig": [
                {
                    "RetryNum": 1
                },
                {
                    "RetryNum": -1
                }
            ]
        },
        "RequestId": "435fbf8e-d512-4f03-baf3-9cf1688f6c98"
    }
}
```

