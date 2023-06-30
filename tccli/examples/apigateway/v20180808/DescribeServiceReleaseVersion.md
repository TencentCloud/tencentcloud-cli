**Example 1: DescribeServiceReleaseVersion**

用户在发布服务时，常有多个版本发布，可使用本接口查询已发布的版本。

Input: 

```
tccli apigateway DescribeServiceReleaseVersion --cli-unfold-argument  \
    --ServiceId service-ody35h5e
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
                    "VersionDesc": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

