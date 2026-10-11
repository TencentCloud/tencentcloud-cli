**Example 1: 开启CLS日志投递请求**



Input: 

```
tccli tione EnableTrainingTaskClsConfig --cli-unfold-argument  \
    --LogEnable True \
    --LogConfig.TopicId topic-123 \
    --LogConfig.LogsetId set-1323 \
    --TaskId train-45235
```

Output: 
```
{
    "Response": {
        "RequestId": "xdsx-fdsa"
    }
}
```

