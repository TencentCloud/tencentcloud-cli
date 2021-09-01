**Example 1: 修改数据库参数**



Input: 

```
tccli dcdb ModifyDBParameters --cli-unfold-argument  \
    --InstanceId dcdbt-ige1a5k3 \
    --Params.0.Param character_set_server \
    --Params.0.Value utf8
```

Output: 
```
{
    "Response": {
        "InstanceId": "dcdbt-ige1a5k3",
        "Result": [
            {
                "Code": 0,
                "Param": "character_set_server"
            }
        ],
        "RequestId": "3381c9e9-d87f-4e21-ba1d-596d6f697a7e"
    }
}
```

