**Example 1: 获取项目环境变量**



Input: 

```
tccli makers DescribeProjectEnvs --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ProjectId makers-************ \
    --Env Production
```

Output: 
```
{
    "Response": {
        "EnvVars": [
            {
                "Comment": null,
                "Env": [
                    "Production"
                ],
                "Id": 2098,
                "Key": "CAPI_TEST",
                "Value": "1"
            }
        ],
        "RequestId": "06a8bdaa-d09c-40ce-949e-7511e1ae7b69"
    }
}
```

