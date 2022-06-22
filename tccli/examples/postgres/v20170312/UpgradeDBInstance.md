**Example 1: 升级实例**



Input: 

```
tccli postgres UpgradeDBInstance --cli-unfold-argument  \
    --Storage 200 \
    --DBInstanceId postgres-6bwgamo3 \
    --Memory 2
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "DealName": "201806127634",
        "BillId": "123"
    }
}
```

