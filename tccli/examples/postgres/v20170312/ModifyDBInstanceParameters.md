**Example 1: 修改实例单个参数**

修改实例max_replication_slots参数值为20

Input: 

```
tccli postgres ModifyDBInstanceParameters --cli-unfold-argument  \
    --DBInstanceId postgres-lzrwgg6d \
    --ParamList.0.Name max_replication_slots \
    --ParamList.0.ExpectedValue 20
```

Output: 
```
{
    "Response": {
        "RequestId": "ec555918-0c22-42ea-aa23-730167195708"
    }
}
```

