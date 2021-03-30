**Example 1: 查询实例信息**



Input: 

```
tccli cdb DescribeDBInstanceInfo --cli-unfold-argument  \
    --InstanceId cdb-oaj9cbla
```

Output: 
```
{
    "Response": {
        "DefaultKmsRegion": "ap-hongkong",
        "Encryption": "NO",
        "InstanceId": "cdb-oaj9cbla",
        "InstanceName": "cdb_name",
        "KeyId": "",
        "KeyRegion": "",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

