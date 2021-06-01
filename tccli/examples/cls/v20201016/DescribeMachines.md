**Example 1: 获取机器状态**



Input: 

```
tccli cls DescribeMachines --cli-unfold-argument  \
    --GroupId 57f5808c-4a55-11eb-b378-0242ac130002
```

Output: 
```
{
    "Response": {
        "Machines": [
            {
                "Ip": "10.10.10.10",
                "Status": 0,
                "Version": "2.1.0",
                "UpdateStatus": 0,
                "ErrCode": 0,
                "ErrMsg": "OK",
                "AutoUpdate": 1,
                "OfflineTime": "2020-12-18 11:17:28"
            }
        ],
        "AutoUpdate": 0,
        "UpdateStartTime": "00:00:00",
        "UpdateEndTime": "01:00:00",
        "LatestAgentVersion": "2.2.0",
        "ServiceLogging": true,
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

