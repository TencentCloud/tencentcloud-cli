**Example 1: 获取访问实例的 URI。**

获取指定实例的 URI 形式的连接串访问地址示例，包含 URI 类型、URI 连接串。

Input: 

```
tccli mongodb DescribeDBInstanceURL --cli-unfold-argument  \
    --InstanceId cmgo-g5*****
```

Output: 
```
{
    "Response": {
        "RequestId": "8e4cb480-9d32-11ec-8dfc-037b69052954",
        "Urls": [
            {
                "Address": "mongodb://mongouser:******@10.*.0.**:27017,10.*.0.**:27017/test?authSource=admin",
                "URLType": "CLUSTER_ALL"
            },
            {
                "Address": "mongodb://mongouser:******@10.*.0.**:27017,10.*.0.**:27017/test?authSource=admin&readPreference=secondaryPreferred",
                "URLType": "CLUSTER_READ_SECONDARY"
            }
        ]
    }
}
```

