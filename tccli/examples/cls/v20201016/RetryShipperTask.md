**Example 1: 重试失败的投递任务**



Input: 

```
tccli cls RetryShipperTask --cli-unfold-argument  \
    --ShipperId xxxxxxxx-xxx-xxx-xxxxxxx \
    --TaskId xxxxxxxx-xxx-xxx-xxxx-xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

