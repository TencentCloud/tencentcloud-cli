**Example 1: 查询AI服务来源列表**

查询AI服务来源列表

Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayAIServiceSourceList --cli-unfold-argument  \
    --GatewayId gateway-4e588095 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "CreateTime": "2026-03-02 20:34:01",
                    "Description": "默认接入点",
                    "SourceId": "source-18fe1a4d31f51d6014ac",
                    "SourceInfo": {},
                    "SourceName": "默认接入点",
                    "SourceProduct": "InnerPolaris",
                    "SourceType": "Registry",
                    "UpdateTime": "2026-03-02 20:34:01"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "6eb4b0b4-cd2f-4c8b-bee1-f40fcdfc7065"
    }
}
```

