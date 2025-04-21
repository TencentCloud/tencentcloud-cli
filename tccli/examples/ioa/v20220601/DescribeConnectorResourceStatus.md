**Example 1: 获取专线分组下连接器到资源的联通状态**

NGN资源联通性链路状态

Input: 

```
tccli ioa DescribeConnectorResourceStatus --cli-unfold-argument  \
    --GroupId xx \
    --ServiceId 0 \
    --PageSize 0 \
    --PageNum 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ConnectorId": "xx",
                    "ConnectorName": "xx",
                    "IsActive": true,
                    "ServiceId": 0,
                    "ReachableState": 0
                }
            ],
            "PageSize": 0,
            "PageNum": 0,
            "PageCount": 0,
            "Total": 0
        },
        "RequestId": "xx"
    }
}
```

