**Example 1: 调整云数据库实例配置**



Input: 

```
tccli mongodb ModifyDBInstanceSpec --cli-unfold-argument  \
    --InstanceId cmgo-p8vnipr5 \
    --Memory 4 \
    --Volume 250
```

Output: 
```
{
    "Response": {
        "RequestId": "d88095e5-50e8-4245-a0cf-993a536f9b20",
        "DealId": "7142863"
    }
}
```

