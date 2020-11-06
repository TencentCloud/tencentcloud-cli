**Example 1: Renaming a TencentDB instance**



Input: 

```
tccli cdb ModifyDBInstanceName --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj \
    --InstanceName 'I am Chinese text'
```

Output: 
```
{
    "Response": {
        "RequestId": "1a42feb9-82087f71-6a0031ac-699a92a8"
    }
}
```

