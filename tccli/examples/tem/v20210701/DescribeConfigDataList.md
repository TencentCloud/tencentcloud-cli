**Example 1: 查询配置列表**

查询配置列表

Input: 

```
tccli tem DescribeConfigDataList --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --ContinueToken token-xxxxxx \
    --Limit 0 \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8b94500c-06cf-42cf-a228-dfea478c3239",
        "Result": {
            "Records": [
                {
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
                },
                {
                    "Name": "pk-test",
                    "CreateTime": "2024-12-19 11:04:13",
                    "RelatedApplications": [],
                    "Data": [
                        {
                            "Key": "name",
                            "Value": "pk",
                            "Type": "",
                            "Config": "",
                            "Secret": ""
                        }
                    ]
                }
            ],
            "RemainingCount": null,
            "ContinueToken": ""
        }
    }
}
```

