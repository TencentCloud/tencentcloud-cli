**Example 1: 隔离MariaDB包年包月实例**

隔离MariaDB包年包月实例

Input: 

```
tccli mariadb IsolateDBInstance --cli-unfold-argument  \
    --InstanceIds tdsql-cq3ndzu7
```

Output: 
```
{
    "Response": {
        "FailedInstanceIds": [],
        "RequestId": "15eec42b-2c7b-410b-8efc-46da52e217a9",
        "SuccessInstanceIds": [
            "tdsql-cq3ndzu7"
        ]
    }
}
```

