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
                    "EnvironmentId": "en-xxxxxx",
                    "Channel": "0",
                    "EnvironmentName": "abc",
                    "Region": "ap-shanghai",
                    "Description": "abc",
                    "Status": 0,
                    "Vpc": "vpc-xxxxxx",
                    "CreateDate": "abc",
                    "ModifyDate": "abc",
                    "Modifier": "abc",
                    "Creator": "abc",
                    "ApplicationNum": 0,
                    "RunInstancesNum": 0,
                    "SubnetId": "abc",
                    "ClusterStatus": "abc",
                    "EnableTswTraceService": true,
                    "Locked": 0,
                    "AppId": "abc",
                    "Uin": "abc",
                    "SubAccountUin": "abc",
                    "ClusterId": "abc",
                    "Tags": [
                        {
                            "TagKey": "abc",
                            "TagValue": "abc"
                        }
                    ],
                    "HasAuthority": true,
                    "EnvType": "abc",
                    "RegionId": "abc"
                }
            ],
            "Total": 0,
            "Size": 0,
            "Pages": 0,
            "Current": 0
        },
        "RequestId": "abc"
    }
}
```

