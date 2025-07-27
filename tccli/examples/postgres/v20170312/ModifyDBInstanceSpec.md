**Example 1: 修改实例配置。**

修改实例postgres-6bwgamo3配置为Cpu1核、内存2GiB、存储200GiB。

Input: 

```
tccli postgres ModifyDBInstanceSpec --cli-unfold-argument  \
    --Storage 200 \
    --DBInstanceId postgres-6bwgamo3 \
    --Cpu 1 \
    --Memory 2
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "DealName": "201806127634",
        "BillId": "20241204591002395368333"
    }
}
```

