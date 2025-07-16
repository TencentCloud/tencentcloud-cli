**Example 1: 开启多可用区部署**

开启多可用区部署

Input: 

```
tccli cynosdb AddClusterSlaveZone --cli-unfold-argument  \
    --ClusterId cynosdbmysql-asd \
    --SlaveZone ap-guangzhou-4 \
    --BinlogSyncWay async \
    --SemiSyncTimeout 10000
```

Output: 
```
{
    "Response": {
        "FlowId": 147184,
        "RequestId": "fd5759b5-89e9-483c-b79c-d99b27c33192"
    }
}
```

