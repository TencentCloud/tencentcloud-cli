**Example 1: 获取环境列表**

获取环境列表

Input: 

```
tccli tem DescribeEnvironments --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "a438e9af-34a0-47d8-bdfc-fc42f652ad6f",
        "Result": {
            "Pages": 1,
            "Records": [
                {
                    "EnvironmentId": "en-xxxxxx",
                    "AppId": "130573xxx",
                    "ApplicationNum": 0,
                    "RunInstancesNum": 0,
                    "Uin": "10001905xxx",
                    "SubAccountUin": "100000799xxx",
                    "EnvironmentName": "test-cluster",
                    "Region": "ap-guangzhou",
                    "RegionId": "1",
                    "Description": "",
                    "ClusterId": "cls-qtqz9mxx",
                    "ClusterStatus": "NORMAL",
                    "Vpc": "vpc-3le4yaxx",
                    "SubnetId": "subnet-pm9fq4xx",
                    "CreateDate": "2024-11-07 16:57:21",
                    "ModifyDate": "2024-11-07 16:57:21",
                    "Modifier": "100019051593",
                    "Creator": "100019051593",
                    "Locked": 0,
                    "Channel": "",
                    "Status": 1,
                    "EnableTswTraceService": false,
                    "Tags": [],
                    "EnvType": "prod",
                    "HasAuthority": true
                }
            ],
            "Total": 1,
            "Size": 20,
            "Current": 1
        }
    }
}
```

