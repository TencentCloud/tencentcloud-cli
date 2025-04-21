**Example 1: cos迁移流程**



Input: 

```
tccli es CreateCosMigrateToServerlessInstance --cli-unfold-argument  \
    --CosBucket user-cos \
    --BasePath dir/ \
    --Snapshot test_snapshot \
    --ServerlessId index-faafeeaf \
    --ClusterInstanceId es-feafaefe \
    --CommonIndexArr test1 \
    --DataStreamArr test1
```

Output: 
```
{
    "Response": {
        "TaskId": "cosMigrateTask-81zl9i82",
        "RequestId": "40f4f780-9969-42f9-8bd9-ccf0d1f2591a"
    }
}
```

