**Example 1: 删除Fleet扩缩容策略配置**

删除Fleet扩缩容策略配置，删除请求服务器舰队fleet-qp3g3caa-ay03mhdm的所有扩缩容策略。

Input: 

```
tccli gse DeleteScalingPolicy --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-ay03mhdm
```

Output: 
```
{
    "Response": {
        "RequestId": "88017b64-f190-4882-9d9c-e995ac565014"
    }
}
```

