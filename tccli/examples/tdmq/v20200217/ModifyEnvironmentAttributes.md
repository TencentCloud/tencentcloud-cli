**Example 1: 修改环境属性**



Input: 

```
tccli tdmq ModifyEnvironmentAttributes --cli-unfold-argument  \
    --EnvironmentId test1 \
    --MsgTTL 3000 \
    --Remark 修改ttl
```

Output: 
```
{
    "Response": {
        "MsgTTL": 3000,
        "EnvironmentId": "test1",
        "Remark": "修改ttl",
        "RequestId": "e5079063-ae7b-45f7-b21f-530cb583cff4"
    }
}
```

