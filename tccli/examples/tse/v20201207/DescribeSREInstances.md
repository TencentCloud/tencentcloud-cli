**Example 1: 查询微服务引擎实例列表**

用于查询微服务引擎实例列表

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
        "Content": [
            {
                "Status": "xx",
                "Paymode": "xx",
                "VpcId": "xx",
                "SpecId": "xx",
                "Name": "xx",
                "EnableStorage": true,
                "InstanceId": "xx",
                "EKSClusterID": "xx",
                "SubnetIds": [
                    "a"
                ],
                "StorageType": "xx",
                "StorageCapacity": 0,
                "Edition": "xx",
                "Replica": 3,
                "EnvInfos": [
                    {
                        "VpcInfos": [
                            {
                                "SubnetId": "xx",
                                "VpcId": "xx"
                            }
                        ],
                        "Status": "xx",
                        "ConfigServiceIp": "xx",
                        "StorageCapacity": 0,
                        "EnvName": "xx",
                        "AdminServiceIp": "xx"
                    }
                ],
                "Type": "xx",
                "CreateTime": "xx"
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

