**Example 1: 获取租户命名空间列表**

获取租户命名空间列表

Input: 

```
tccli tem DescribeNamespaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "Records": [
                {
                    "Status": 0,
                    "ModifyDate": "xx",
                    "Description": "xx",
                    "Creator": "xx",
                    "CreateDate": "xx",
                    "NamespaceName": "xx",
                    "Region": "xx",
                    "EnableTswTraceService": true,
                    "TcbEnvStatus": "xx",
                    "ServiceNum": 0,
                    "RunInstancesNum": 0,
                    "Vpc": "xx",
                    "SubnetId": "xx",
                    "ClusterStatus": "xx",
                    "Modifier": "xx",
                    "NamespaceId": "xx",
                    "Channel": "xx"
                }
            ],
            "Total": 0,
            "Pages": 0,
            "Size": 0
        },
        "RequestId": "xx"
    }
}
```

