**Example 1: DescribeMessageRouteList**



Input: 

```
tccli iecp DescribeMessageRouteList --cli-unfold-argument  \
    --Filter a \
    --Limit 10 \
    --StartTime xx \
    --Offset 0 \
    --EndTime - \
    --Order DESC
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RouteList": [
            {
                "Status": "off",
                "SourceUnitIDList": [],
                "SourceUnitNameList": [],
                "MessageCount": 0,
                "TopicFilter": "0data",
                "SourceProductName": "cp",
                "Descript": "",
                "MessageLastTime": "",
                "RouteID": 1000000,
                "Healthy": "yes",
                "RouteName": "a",
                "SourceProductID": "KMUOZ5EOXH",
                "Mode": "topic-datasource",
                "TargetOptions": "{\"DataSourceId\":1000000}",
                "SourceDeviceNameList": [
                    "cpp"
                ],
                "CreateTime": "2022-02-25 11:31:00"
            }
        ],
        "RequestId": "6aab2bdf-5f76-464b-859f-470e765d29e8"
    }
}
```

