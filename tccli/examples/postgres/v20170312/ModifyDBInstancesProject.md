**Example 1: 将实例转至其他项目**



Input: 

```
tccli postgres ModifyDBInstancesProject --cli-unfold-argument  \
    --DBInstanceIdSet postgres-6bwgamo3 postgres-lnp6j6172\
    --ProjectId 10467
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
    --DBInstanceIdSet postgres-6bwgamo3\
    --ProjectId 10467
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "Error": {
            "Message": "Failed to get instance",
            "Code": "InternalError.DBError"
        }
    }
}
```

