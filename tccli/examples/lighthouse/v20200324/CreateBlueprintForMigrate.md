**Example 1: 通过在线迁移临时实例创建自定义镜像**



Input: 

```
tccli lighthouse CreateBlueprintForMigrate --cli-unfold-argument  \
    --BlueprintName test-0006 \
    --InstanceId lhmins-m9oaw2cp
```

Output: 
```
{
    "Response": {
        "BlueprintId": "lhbp-i7vqx7r5",
        "RequestId": "e4907750-3aa0-488d-a146-aeab66513441"
    }
}
```

