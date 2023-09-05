**Example 1: 开启多可用区部署**

开启多可用区部署

Input: 

```
tccli cynosdb AddClusterSlaveZone --cli-unfold-argument  \
    --ClusterId cynosdbmysql-asd \
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

