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
            "Current": 0,
            "Records": [
                {
                    "SubAccountUin": "xx",
                    "Channel": "xx",
                    "Status": 0,
                    "EnvironmentName": "xx",
                    "HasAuthority": true,
                    "ModifyDate": "xx",
                    "Description": "xx",
                    "Tags": [
                        {
                            "TagKey": "xx",
                            "TagValue": "xx"
                        }
                    ],
                    "RegionId": "xx",
                    "ClusterId": "xx",
                    "RunInstancesNum": 0,
                    "Vpc": "xx",
                    "SubnetId": "xx",
                    "CreateDate": "xx",
                    "Locked": 0,
                    "Region": "xx",
                    "EnableTswTraceService": true,
                    "Modifier": "xx",
                    "EnvironmentId": "xx",
                    "Creator": "xx",
                    "EnvType": "xx",
                    "Uin": "xx",
                    "AppId": "xx",
                    "ClusterStatus": "xx",
                    "ApplicationNum": 0
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

