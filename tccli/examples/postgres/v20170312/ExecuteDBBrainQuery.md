**Example 1: 执行DBBrain查询SQL**

用于DBBrain侧获取实例相关数据的SQL执行

Input: 

```
tccli postgres ExecuteDBBrainQuery --cli-unfold-argument  \
    --DBInstanceId postgres-nv3mfnkx \
    --SqlNo 31 \
    --NodeRole master \
    --Args 10 \
    --Filters.0.Name datname \
    --Filters.0.Values postgres \
    --Filters.0.Operate not_eq
```

Output: 
```
{
    "Response": {
        "Data": [],
        "Message": "Success",
        "Names": [],
        "RequestId": "4360d27d-8161-4f2f-b50e-573121ecc762"
    }
}
```

