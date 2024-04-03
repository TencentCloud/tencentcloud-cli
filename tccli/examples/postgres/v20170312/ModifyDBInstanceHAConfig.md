**Example 1: 修改为异步**

主从同步方式采用异步，设置允许切换的最大延迟

Input: 

```
tccli postgres ModifyDBInstanceHAConfig --cli-unfold-argument  \
    --DBInstanceId postgres-32d4mmv9 \
    --SyncMode Async \
    --MaxStandbyLatency 10737418240 \
    --MaxStandbyLag 10
```

Output: 
```
{
    "Response": {
        "RequestId": "c4676122-1694-4d0f-8b03-a33b4e1bd850"
    }
}
```

**Example 2: 修改为半同步，允许退化为异步复制**

主从同步方式采用半同步，设置允许切换的最大延迟，允许退化为异步复制

Input: 

```
tccli postgres ModifyDBInstanceHAConfig --cli-unfold-argument  \
    --DBInstanceId postgres-32d4mmv9 \
    --SyncMode Semi-sync \
    --MaxStandbyLatency 10737418240 \
    --MaxStandbyLag 10 \
    --MaxSyncStandbyLatency 1073741824 \
    --MaxSyncStandbyLag 5
```

Output: 
```
{
    "Response": {
        "RequestId": "34c1d54c-ea3e-4594-8a5d-1b739123949d"
    }
}
```

**Example 3: 修改为半同步，禁止退化为异步复制**

主从同步方式采用半同步，设置允许切换的最大延迟，禁止退化为异步复制

Input: 

```
tccli postgres ModifyDBInstanceHAConfig --cli-unfold-argument  \
    --DBInstanceId postgres-32d4mmv9 \
    --SyncMode Semi-sync \
    --MaxStandbyLatency 10737418240 \
    --MaxStandbyLag 10
```

Output: 
```
{
    "Response": {
        "RequestId": "9b923bd9-6a3b-482a-945d-ea2e6f2a9f17"
    }
}
```

