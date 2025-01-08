**Example 1: 示例**

拉取独立网关云托管的配置信息

Input: 

```
tccli tcb DescribeCloudBaseRunConfForGateWay --cli-unfold-argument  \
    --EnvID env-sdff \
    --VpcID vpc-sdfsdf
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "EnvId": "env-sdfd",
                "GrayKey": "",
                "Weight": 100,
                "ServerName": "server",
                "AccessType": 2,
                "LbAddr": "",
                "IsZero": false,
                "GrayType": "",
                "VersionName": "verison",
                "URLs": [],
                "IsDefault": false,
                "GrayValue": "",
                "ConfigType": 0
            }
        ],
        "RequestId": "sfafsaf",
        "LastUpTime": ""
    }
}
```

