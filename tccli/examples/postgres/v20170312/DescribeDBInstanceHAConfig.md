**Example 1: 允许退化为异步的半同步实例，查询HA配置**

根据实例ID查询HA配置，该实例采用半同步复制，允许退化为异步复制

Input: 

```
tccli postgres DescribeDBInstanceHAConfig --cli-unfold-argument  \
    --DBInstanceId postgres-32d4mmv9
```

Output: 
```
{
    "Response": {
        "MaxStandbyLag": 10,
        "MaxStandbyLatency": 10737418240,
        "MaxSyncStandbyLag": 5,
        "MaxSyncStandbyLatency": 1073741824,
        "RequestId": "897783db-0451-479b-a205-b2b0e48d29a8",
        "SyncMode": "Semi-sync"
    }
}
```

**Example 2: 异步实例，查询HA配置**

根据实例ID查询HA配置，该实例采用异步复制

Input: 

```
tccli postgres DescribeDBInstanceHAConfig --cli-unfold-argument  \
    --DBInstanceId postgres-32d4mmv9
```

Output: 
```
{
    "Response": {
        "MaxStandbyLag": 10,
        "MaxStandbyLatency": 10737418240,
        "MaxSyncStandbyLag": null,
        "MaxSyncStandbyLatency": null,
        "RequestId": "730627a4-547d-422b-8aac-239041b12212",
        "SyncMode": "Async"
    }
}
```

**Example 3: 禁止退化为异步的半同步实例，查询HA配置**

根据实例ID查询HA配置，该实例采用半同步复制，禁止退化为异步复制

Input: 

```
tccli postgres DescribeDBInstanceHAConfig --cli-unfold-argument  \
    --DBInstanceId postgres-32d4mmv9
```

Output: 
```
{
    "Response": {
        "MaxStandbyLag": 10,
        "MaxStandbyLatency": 10737418240,
        "MaxSyncStandbyLag": null,
        "MaxSyncStandbyLatency": null,
        "RequestId": "a5399d5a-c77b-4c57-9a17-790e9c61ab33",
        "SyncMode": "Semi-sync"
    }
}
```

