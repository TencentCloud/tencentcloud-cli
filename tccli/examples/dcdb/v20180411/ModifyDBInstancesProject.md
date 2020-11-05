**Example 1: Modifying the project to which TencentDB instances belong**



Input: 

```
tccli dcdb ModifyDBInstancesProject --cli-unfold-argument  \
    --InstanceIds dcdbt-fdpjf5zh\
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

