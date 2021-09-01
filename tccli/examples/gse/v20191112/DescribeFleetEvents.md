**Example 1: 查询服务器舰队的事件列表**

本示例用于查看服务器舰队的事件列表

Input: 

```
tccli gse DescribeFleetEvents --cli-unfold-argument  \
    --FleetId fleet-pro4extc-kej8s8z4 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "EventCode": "FLEET_STATE_VALIDATING",
                "EventId": "event-qyylnmcz-cic9i6f3",
                "EventTime": "2019-12-09T06:10:29Z",
                "Message": "Fleet changed state to VALIDATING",
                "PreSignedLogUrl": "",
                "ResourceId": "fleet-pro4extc-kej8s8z4"
            },
            {
                "EventCode": "FLEET_CREATION_RUNNING_INSTALLER",
                "EventId": "event-qyylnmcz-2nweakep",
                "EventTime": "2019-12-09T06:08:29Z",
                "Message": "Running installer at /local/game/install.sh",
                "PreSignedLogUrl": "",
                "ResourceId": "fleet-pro4extc-kej8s8z4"
            },
            {
                "EventCode": "FLEET_CREATION_VALIDATING_RUNTIME_CONFIG",
                "EventId": "event-qyylnmcz-g8qtc5wd",
                "EventTime": "2019-12-09T06:08:29Z",
                "Message": "Searching for runtime path.",
                "PreSignedLogUrl": "",
                "ResourceId": "fleet-pro4extc-kej8s8z4"
            },
            {
                "EventCode": "FLEET_STATE_DOWNLOADING",
                "EventId": "event-qyylnmcz-npk9jmjb",
                "EventTime": "2019-12-09T06:05:29Z",
                "Message": "Fleet  changed state to DOWNLOADING",
                "PreSignedLogUrl": "",
                "ResourceId": "fleet-pro4extc-kej8s8z4"
            },
            {
                "EventCode": "FLEET_CREATED",
                "EventId": "event-qyylnmcz-ibwl3703",
                "EventTime": "2019-12-09T06:01:29Z",
                "Message": "Fleet has been created with state NEW.",
                "PreSignedLogUrl": "",
                "ResourceId": "fleet-pro4extc-kej8s8z4"
            },
            {
                "EventCode": "FLEET_CREATION_EXTRACTING_BUILD",
                "EventId": "event-qyylnmcz-1gwrgqmr",
                "EventTime": "2019-12-09T06:01:29Z",
                "Message": "Extracting Build.",
                "PreSignedLogUrl": "",
                "ResourceId": "fleet-pro4extc-kej8s8z4"
            }
        ],
        "RequestId": "s1575880419614511725",
        "TotalCount": 6
    }
}
```

