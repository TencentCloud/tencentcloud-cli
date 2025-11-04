**Example 1: 升级3.6版本实例到4.0版本**

用于MongoDB数据库3.6版本升级到4.0版本

Input: 

```
tccli mongodb UpgradeDbInstanceVersion --cli-unfold-argument  \
    --InstanceId cmgo-p8vnipr5 \
    --MongoVersion MONGO_42_WT
```

Output: 
```
{
    "Response": {
        "RequestId": "2efcf780-9970-11ec-8975-6bc44e3bfad7",
        "FlowId": 19677
    }
}
```

