**Example 1: Modifying database parameters**



Input: 

```
tccli mariadb ModifyDBParameters --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3\
    --Params.0.Param character_set_server\
    --Params.0.Value utf8
```

Output: 
```
{
    "Response": {
        "InstanceId": "tdsql-ige1a5k3",
        "Config": [
            {
                "Code": 0,
                "Param": "character_set_server"
            }
        ],
        "RequestId": "896e21bc-1547-4ce2-ab81-c97cc9d73973"
    }
}
```

