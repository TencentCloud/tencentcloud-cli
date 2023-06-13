**Example 1: 批量修改实例项目**

批量修改实例项目

Input: 

```
tccli postgres ModifyDBInstancesProject --cli-unfold-argument  \
    --ProjectId 10467 \
    --DBInstanceIdSet postgres-lnp6j6172 postgres-6bwgamo3
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "Count": 2
    }
}
```

