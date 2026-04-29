**Example 1: 获取业务资源**

Path : /capi/GatewayResource/DescribeBusinessResources

Input: 

```
tccli ioa DescribeBusinessResources --cli-unfold-argument  \
    --AreaId 108 \
    --ServiceName 名称 \
    --Keywords 资源 \
    --StartTime 2002-01-02 15:04:05 \
    --EndTime 2022-07-02 15:04:05 \
    --Condition.Sort.Field Level \
    --Condition.Sort.Order desc \
    --Condition.PageNum 0 \
    --Condition.PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Levels": 5000,
                    "SmartGateNames": "网关名称",
                    "CreateTime": "2022-07-21 10:24:43",
                    "DetectState": 1,
                    "DetectInfo": "[]",
                    "DetectTime": "2022-07-21 10:24:43",
                    "AreaId": 108,
                    "ServiceId": 62,
                    "ServiceName": "资源名称",
                    "ServiceType": "domain",
                    "ServiceAddress": "*.baidu.com",
                    "DirectConn": 0,
                    "ServicePort": "all",
                    "UpdateTime": "2022-07-21 10:24:43",
                    "Remark": "",
                    "SmartGateIds": [
                        1
                    ],
                    "Protocol": 2
                }
            ]
        },
        "RequestId": "1658370329.784533"
    }
}
```

