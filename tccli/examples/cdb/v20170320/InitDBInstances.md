**Example 1: Initializing a new instance**



Input: 

```
tccli cdb InitDBInstances --cli-unfold-argument  \
    --InstanceIds cdb-f35wr6wj \
    --NewPassword Gx18ux23F^X \
    --Parameters.0.name lower_case_table_names \
    --Parameters.0.value 1 \
    --Parameters.1.name character_set_server \
    --Parameters.1.value utf8
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestIds": [
            "8cd119d4-61ba-11e7-aeff-018cfa1f5560"
        ]
    }
}
```

