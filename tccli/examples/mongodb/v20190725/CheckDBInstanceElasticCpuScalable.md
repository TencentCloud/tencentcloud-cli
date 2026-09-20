**Example 1: 查询实例是否可开启弹性cpu扩容**



Input: 

```
tccli mongodb CheckDBInstanceElasticCpuScalable --cli-unfold-argument  \
    --InstanceId cmgo-********
```

Output: 
```
{
    "Response": {
        "ExtraCpu": 6,
        "IsLocked": false,
        "IsScaled": true,
        "MaxExtraCpu": 4,
        "Reason": "Instance is already in scaled state",
        "Scalable": false,
        "ScaleUpTime": "2026-02-28 10:31:09",
        "TriggerType": 1,
        "RequestId": "efb92d21-55ba-4054-87a9-8f776b4afb32"
    }
}
```

