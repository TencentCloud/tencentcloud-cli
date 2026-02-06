**Example 1: 修改数据库参数**



Input: 

```
tccli tdmysql ModifyDBParameters --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3 \
    --Params.0.Param character_set_server \
    --Params.0.Value utf
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TaskID": 123
    }
}
```

