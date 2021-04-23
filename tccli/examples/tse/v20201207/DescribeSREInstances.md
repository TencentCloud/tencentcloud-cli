**Example 1: 查询微服务注册引擎实例列表**

用于查询微服务注册引擎实例列表

Input: 

```
tccli tse DescribeSREInstances --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e05507e42d5970cd2e25ed1167a",
        "TotalCount": 0,
        "Content": [
            {
                "InstanceId": "sre-qfv8fkxxx",
                "Name": "test",
                "Edition": "1.8.6",
                "Type": "consul",
                "Status": "creating",
                "SpecId": "spec-ajfkxxx",
                "Replica": 3,
                "SubnetIds": [
                    "a"
                ],
                "VpcId": "vpc-123456",
                "EnableStorage": true,
                "StorageType": "xx",
                "StorageCapacity": 0,
                "Paymode": "xx"
            }
        ]
    }
}
```

