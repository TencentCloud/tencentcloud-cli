**Example 1: DescribeServiceEnvironmentReleaseHistory**

用于查询服务环境的发布历史。

Input: 

```
tccli apigateway DescribeServiceEnvironmentReleaseHistory --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --EnvironmentName test
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "VersionList": [
                {
                    "VersionName": "abc",
                    "VersionDesc": "abc",
                    "ReleaseTime": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

