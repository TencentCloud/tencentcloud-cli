**Example 1: 请求示例**



Input: 

```
tccli redis UpgradeInstance --cli-unfold-argument  \
    --InstanceId crs-5qlr**** \
    --MemSize 4096 \
    --RedisShardNum 5 \
    --RedisReplicasNum 3
```

Output: 
```
{
    "Response": {
        "DealId": "6954227",
        "RequestId": "4daddc97-0005-45d8-b5b8-38514ec1e97c"
    }
}
```

