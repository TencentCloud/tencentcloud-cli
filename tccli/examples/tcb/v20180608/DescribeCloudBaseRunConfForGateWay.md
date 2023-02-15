**Example 1: 示例**

拉取独立网关云托管的配置信息

Input: 

```
tccli tcb DescribeCloudBaseRunConfForGateWay --cli-unfold-argument  \
    --EnvID xx \
    --VpcID xx
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "EnvId": "xx",
                "GrayKey": "xx",
                "Weight": 100,
                "ServerName": "xx",
                "AccessType": 2,
                "LbAddr": "xx",
                "IsZero": false,
                "GrayType": "xx",
                "VersionName": "xx",
                "URLs": [
                    "xx"
                ],
                "IsDefault": false,
                "GrayValue": "xx"
            }
        ],
        "RequestId": "xx",
        "LastUpTime": "xx"
    }
}
```

