**Example 1: 将实例转至其他项目**



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

**Example 2: 将实例postgres-6bwgamo3转移至项目ID为10467的项目里面去**



Input: 

```
tccli postgres ModifyDBInstancesProject --cli-unfold-argument  \
    --ProjectId 10467 \
    --DBInstanceIdSet postgres-6bwgamo3
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

