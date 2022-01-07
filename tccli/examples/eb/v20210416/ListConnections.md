**Example 1: 获取连接器列表**



Input: 

```
tccli eb ListConnections --cli-unfold-argument  \
    --EventBusId eb-l65vlc2
```

Output: 
```
{
    "Response": {
        "Connections": [],
        "RequestId": "cec4c711-4e68-43ac-988f-00171f2b2146",
        "TotalCount": 0
    }
}
```

**Example 2: 获取连接器列表1**



Input: 

```
tccli eb ListConnections --cli-unfold-argument  \
    --EventBusId eb-l65vlc2
```

Output: 
```
{
    "Response": {
        "Connections": [
            {
                "AddTime": "2021-04-29T13:13:43+08:00",
                "ConnectionDescription": {
                    "APIGWParams": null,
                    "ResourceDescription": "qcs::tdmq:ap-guangzhou:uin/3473058547:subscriptionName/pulsar-5r5drqo7j8/user/test/sub1"
                },
                "ConnectionId": "connection-5t492ybt",
                "ConnectionName": "conn",
                "Description": "",
                "Enable": false,
                "EventBusId": "eb-l65vlc2u",
                "ModTime": "2021-04-29T13:13:44+08:00",
                "Status": "Active",
                "Type": "tdmq"
            },
            {
                "AddTime": "2021-04-29T13:00:32+08:00",
                "ConnectionDescription": {
                    "APIGWParams": null,
                    "ResourceDescription": "qcs::tdmq:ap-guangzhou:uin/3473058547:subscriptionName/pulsar-5r5drqo7j8/user/test/sub1"
                },
                "ConnectionId": "connection-7mpfojtt",
                "ConnectionName": "conn",
                "Description": "",
                "Enable": false,
                "EventBusId": "eb-l65vlc2u",
                "ModTime": "2021-04-29T13:00:33+08:00",
                "Status": "Failed",
                "Type": "tdmq"
            },
            {
                "AddTime": "2021-04-29T12:58:24+08:00",
                "ConnectionDescription": {
                    "APIGWParams": null,
                    "ResourceDescription": "qcs::tdmq:ap-guangzhou:uin/3473058547:subscriptionName/pulsar-5r5drqo7j8/user/test/sub1"
                },
                "ConnectionId": "connection-il11bb0h",
                "ConnectionName": "conn",
                "Description": "",
                "Enable": false,
                "EventBusId": "eb-l65vlc2u",
                "ModTime": "2021-04-29T12:58:24+08:00",
                "Status": "Failed",
                "Type": "tdmq"
            },
            {
                "AddTime": "2021-04-29T12:01:34+08:00",
                "ConnectionDescription": {
                    "APIGWParams": null,
                    "ResourceDescription": "qcs::tdmq:ap-guangzhou:uin/3473058547:subscriptionName/pulsar-5r5drqo7j8/user/test/sub1"
                },
                "ConnectionId": "connection-6s29eqob",
                "ConnectionName": "conn",
                "Description": "",
                "Enable": false,
                "EventBusId": "eb-l65vlc2u",
                "ModTime": "2021-04-29T12:01:35+08:00",
                "Status": "Failed",
                "Type": "tdmq"
            },
            {
                "AddTime": "2021-04-29T11:46:27+08:00",
                "ConnectionDescription": {
                    "APIGWParams": null,
                    "ResourceDescription": "qcs::tdmq:ap-guangzhou:uin/3473058547:subscriptionName/pulsar-5r5drqo7j8/user/test/sub1"
                },
                "ConnectionId": "connection-dka58wiv",
                "ConnectionName": "conn",
                "Description": "",
                "Enable": false,
                "EventBusId": "eb-l65vlc2u",
                "ModTime": "2021-04-29T11:46:28+08:00",
                "Status": "Failed",
                "Type": "tdmq"
            },
            {
                "AddTime": "2021-04-29T11:42:44+08:00",
                "ConnectionDescription": {
                    "APIGWParams": null,
                    "ResourceDescription": "qcs::tdmq:ap-guangzhou:uin/3473058547:subscriptionName/pulsar-5r5drqo7j8/user/test/sub1"
                },
                "ConnectionId": "connection-r1o76r2d",
                "ConnectionName": "conn",
                "Description": "",
                "Enable": false,
                "EventBusId": "eb-l65vlc2u",
                "ModTime": "2021-04-29T11:42:44+08:00",
                "Status": "Failed",
                "Type": "tdmq"
            },
            {
                "AddTime": "2021-04-29T11:35:12+08:00",
                "ConnectionDescription": {
                    "APIGWParams": null,
                    "ResourceDescription": "qcs::tdmq:ap-guangzhou:uin/3473058547:subscriptionName/pulsar-5r5drqo7j8/user/test/sub1"
                },
                "ConnectionId": "connection-ay3ix129",
                "ConnectionName": "conn",
                "Description": "",
                "Enable": false,
                "EventBusId": "eb-l65vlc2u",
                "ModTime": "2021-04-29T11:35:13+08:00",
                "Status": "Failed",
                "Type": "tdmq"
            },
            {
                "AddTime": "2021-04-29T11:24:45+08:00",
                "ConnectionDescription": {
                    "APIGWParams": null,
                    "ResourceDescription": "qcs::tdmq:ap-guangzhou:uin/3473058547:subscriptionName/pulsar-5r5drqo7j8/user/test/sub1"
                },
                "ConnectionId": "connection-heno97b7",
                "ConnectionName": "conn",
                "Description": "",
                "Enable": false,
                "EventBusId": "eb-l65vlc2u",
                "ModTime": "2021-04-29T11:24:45+08:00",
                "Status": "Failed",
                "Type": "tdmq"
            }
        ],
        "RequestId": "e576a375-88ae-4c3f-84a9-0bf28dc7b0ee",
        "TotalCount": 8
    }
}
```

