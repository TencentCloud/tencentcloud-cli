**Example 1: 获取环境列表**

获取环境列表

Input: 

```
tccli tem DescribeEnvironments --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "Records": [
                {
                    "Status": 0,
                    "EnvironmentId": "xx",
                    "Locked": 0,
                    "Description": "xx",
                    "EnvironmentName": "xx",
                    "Region": "xx",
                    "Creator": "xx",
                    "EnableTswTraceService": true,
                    "RunInstancesNum": 0,
                    "Vpc": "xx",
                    "ModifyDate": "xx",
                    "SubnetId": "xx",
                    "ClusterStatus": "xx",
                    "Modifier": "xx",
                    "ApplicationNum": 0,
                    "CreateDate": "xx",
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

