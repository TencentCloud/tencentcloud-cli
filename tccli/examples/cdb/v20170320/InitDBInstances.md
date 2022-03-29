**Example 1: 初始化新实例**



Input: 

```
tccli cdb InitDBInstances --cli-unfold-argument  \
    --NewPassword xx \
    --Vport 0 \
    --Parameters.0.Name lower_case_table_names \
    --Parameters.0.Value 1 \
    --Parameters.1.Name character_set_server \
    --Parameters.1.Value utf8 \
    --InstanceIds cdb-f35wr6wj
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

