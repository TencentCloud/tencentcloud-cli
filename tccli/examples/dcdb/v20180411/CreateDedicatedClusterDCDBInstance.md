**Example 1: 创建TDSQL独享集群实例**

创建TDSQL独享集群实例

Input: 

```
tccli dcdb CreateDedicatedClusterDCDBInstance --cli-unfold-argument  \
    --Zone ap-guangzhou-2 \
    --ClusterId cage-shjr-2-15 \
    --GoodsNum 1 \
    --ShardNum 2 \
    --ShardMemory 2 \
    --ShardStorage 10 \
    --Pid 100
```

Output: 
```
{
    "Response": {
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6",
        "InstanceIds": [
            "tdsql-xxxxxx"
        ],
        "FlowId": 1122
    }
}
```

