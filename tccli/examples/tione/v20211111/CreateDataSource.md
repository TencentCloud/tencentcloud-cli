**Example 1: 成功示例**



Input: 

```
tccli tione CreateDataSource --cli-unfold-argument  \
    --Name 测试数据源 \
    --Type Cfs \
    --Permission RW \
    --StorageId cfs-ndqrxskx \
    --MountConfigure.WorkDir /abc \
    --Tags.0.TagKey key1 \
    --Tags.0.TagValue value2
```

Output: 
```
{
    "Response": {
        "Id": "dsrc-Cfs-abum82k1s7wg",
        "RequestId": "e3c94882-87a2-445e-80b3-2f8d3558f9dd"
    }
}
```

