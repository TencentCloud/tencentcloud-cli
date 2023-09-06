**Example 1: 关闭多可用区部署**



Input: 

```
tccli cynosdb RemoveClusterSlaveZone --cli-unfold-argument  \
    --ClusterId cynosdmysql-asd \
    --SlaveZone ap-guangzhou-4
```

Output: 
```
{
    "Response": {
        "FlowId": 123,
        "RequestId": "128046"
    }
}
```

