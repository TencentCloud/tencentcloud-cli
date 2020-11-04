**Example 1: 获取实例基本信息**



Input: 

```
tccli cdb DescribeDBInstanceInfo --cli-unfold-argument  \
    --InstanceId cdb-***
```

Output: 
```
{
    "Response": {
        "InstanceId": "test",
        "InstanceName": "test",
        "Encryption": "YES",
        "KeyId": "sdasdd-12asdasd",
        "KeyRegion": "ap-guangzhou",
        "RequestId": "faae8d6a-38fb-44de-988e-5a0e78aba4a7"
    }
}
```

