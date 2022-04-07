**Example 1: DescribeMessageRouteList**



Input: 

```
tccli iecp DescribeMessageRouteList --cli-unfold-argument  \
    --Filter xx \
    --Limit 0 \
    --StartTime xx \
    --Offset 0 \
    --EndTime xx \
    --Order xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RouteList": [
            {
                "Status": "xx",
                "SourceUnitIDList": [
                    "xx"
                ],
                "SourceUnitNameList": [
                    "xx"
                ],
                "MessageCount": 0,
                "TopicFilter": "xx",
                "SourceProductName": "xx",
                "Descript": "xx",
                "MessageLastTime": "xx",
                "RouteID": 0,
                "Healthy": "xx",
                "RouteName": "xx",
                "SourceProductID": "xx",
                "Mode": "xx",
                "TargetOptions": "xx",
                "SourceDeviceNameList": [
                    "xx"
                ],
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

