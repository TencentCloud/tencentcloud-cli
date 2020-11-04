**Example 1: 解隔离云数据库实例**



Input: 

```
tccli cdb ReleaseIsolatedDBInstances --cli-unfold-argument  \
    --InstanceIds cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "RequestId": "eeab769d-0c08-456a-971f-dc24f4c585c8",
        "Items": [
            {
                "InstanceId": "cdb-f35wr6wj",
                "Code": 0,
                "Message": "ok"
            }
        ]
    }
}
```

