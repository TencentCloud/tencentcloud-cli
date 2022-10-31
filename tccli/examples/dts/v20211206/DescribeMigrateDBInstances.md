**Example 1: 查询迁移实例列表**

查询迁移实例列表

Input: 

```
tccli dts DescribeMigrateDBInstances --cli-unfold-argument  \
    --InstanceId cdb-eur39922 \
    --DatabaseType mysql \
    --MigrateRole src
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "cafebabe-848392-di98382-dfu9832",
        "Instances": []
    }
}
```

