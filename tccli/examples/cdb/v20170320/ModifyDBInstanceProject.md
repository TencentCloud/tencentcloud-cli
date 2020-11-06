**Example 1: Modifying the project to which a TencentDB instance belongs**



Input: 

```
tccli cdb ModifyDBInstanceProject --cli-unfold-argument  \
    --InstanceIds cdb-f35wr6wj \
    --NewProjectId 12
```

Output: 
```
{
    "Response": {
        "RequestId": "1a42feb9-82087f71-6a0031ac-699a92a8"
    }
}
```

