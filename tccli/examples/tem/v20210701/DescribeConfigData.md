**Example 1: 查询配置详情**

查询配置详情

Input: 

```
tccli tem DescribeConfigData --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --Name abc-xxxx \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8b94500c-06cf-42cf-a228-dfea478c3239",
        "Result": {
            "Name": "config-test",
            "CreateTime": "2024-12-19 23:55:05",
            "RelatedApplications": [],
            "Data": [
                {
                    "Key": "key-xxx",
                    "Value": "val-xxx",
                    "Type": "",
                    "Config": "",
                    "Secret": ""
                }
            ]
        }
    }
}
```

