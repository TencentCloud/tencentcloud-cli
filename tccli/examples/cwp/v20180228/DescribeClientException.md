**Example 1: 示例1**



Input: 

```
tccli cwp DescribeClientException --cli-unfold-argument  \
    --EndTime  \
    --Limit 10 \
    --ExceptionType 1 \
    --StartTime  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "HostIP": "172.23.16.2",
                "InstanceID": "ins-kz85kljw",
                "Uuid": "2e6353e4-0498-450a-9be5-77e2537247f6",
                "OfflineTime": "2022-04-24T17:52:37+08:00",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "172.23.16.2",
                "InstanceID": "ins-kz85kljw",
                "Uuid": "2e6353e4-0498-450a-9be5-77e2537247f6",
                "OfflineTime": "2022-04-24T19:15:03+08:00",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "172.23.16.2",
                "InstanceID": "ins-kz85kljw",
                "Uuid": "2e6353e4-0498-450a-9be5-77e2537247f6",
                "OfflineTime": "2022-04-24T19:30:19+08:00",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "172.23.16.2",
                "InstanceID": "ins-kz85kljw",
                "Uuid": "2e6353e4-0498-450a-9be5-77e2537247f6",
                "OfflineTime": "2022-04-24T20:07:44+08:00",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "172.23.16.2",
                "InstanceID": "ins-kz85kljw",
                "Uuid": "2e6353e4-0498-450a-9be5-77e2537247f6",
                "OfflineTime": "2022-04-25T10:58:57+08:00",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "",
                "InstanceID": "",
                "Uuid": "5878d9b1-6304-49a0-849b-c9f2132048a5",
                "OfflineTime": "2022-04-27T20:35:57+08:00",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "10.0.0.6",
                "InstanceID": "ins-7pl19k95",
                "Uuid": "13bb1e16-9a7a-434d-9686-4328f72c97d7",
                "OfflineTime": "2022-05-01T00:55:13+08:00",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "10.0.22.29",
                "InstanceID": "ins-g91krvsw",
                "Uuid": "71b1d8d3-8a69-4af6-9e95-f1637096c904",
                "OfflineTime": "2022-05-01T11:25:03+08:00",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "10.0.22.29",
                "InstanceID": "ins-g91krvsw",
                "Uuid": "71b1d8d3-8a69-4af6-9e95-f1637096c904",
                "OfflineTime": "2022-05-01T12:29:54+08:00",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "10.0.22.29",
                "InstanceID": "ins-g91krvsw",
                "Uuid": "71b1d8d3-8a69-4af6-9e95-f1637096c904",
                "OfflineTime": "2022-05-01T12:29:54+08:00",
                "UninstallTime": "",
                "UninstallCmd": ""
            }
        ],
        "RequestId": "1248a7df-c3fe-4930-b3ff-2af956cf8d66",
        "TotalCount": 944
    }
}
```

**Example 2: 示例2**



Input: 

```
tccli cwp DescribeClientException --cli-unfold-argument  \
    --EndTime  \
    --Limit 10 \
    --ExceptionType 1 \
    --StartTime  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "HostIP": "172.16.48.110",
                "InstanceID": "ins-7kdvmxgi",
                "Uuid": "946b0a12-4005-443b-9d0e-a2795d52a8fb",
                "OfflineTime": "2022-11-15 22:25:05",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "10.0.22.33",
                "InstanceID": "ins-bmavftgm",
                "Uuid": "e3fddc1e-c2da-431e-9e1b-adfd70cd208c",
                "OfflineTime": "2022-11-14 17:35:40",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "10.0.0.7",
                "InstanceID": "ins-pgro6nri",
                "Uuid": "2651386e-e6cf-4e32-ac8e-3bd59e920d27",
                "OfflineTime": "2022-11-14 17:33:04",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "10.0.22.10",
                "InstanceID": "ins-lukah9oq",
                "Uuid": "2819e736-eb93-4912-a82a-2eac7c1788b0",
                "OfflineTime": "2022-11-14 17:31:35",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "172.23.0.36",
                "InstanceID": "ins-g4l64238",
                "Uuid": "c90117e5-6609-4ad6-b347-7a601dbb81f6",
                "OfflineTime": "2022-11-14 17:29:58",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "172.23.0.36",
                "InstanceID": "ins-g4l64238",
                "Uuid": "c90117e5-6609-4ad6-b347-7a601dbb81f6",
                "OfflineTime": "2022-11-14 14:53:56",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "172.16.48.110",
                "InstanceID": "ins-7kdvmxgi",
                "Uuid": "946b0a12-4005-443b-9d0e-a2795d52a8fb",
                "OfflineTime": "2022-11-14 14:26:23",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "172.23.0.36",
                "InstanceID": "ins-g4l64238",
                "Uuid": "c90117e5-6609-4ad6-b347-7a601dbb81f6",
                "OfflineTime": "2022-11-14 13:15:22",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "172.23.0.36",
                "InstanceID": "ins-g4l64238",
                "Uuid": "c90117e5-6609-4ad6-b347-7a601dbb81f6",
                "OfflineTime": "2022-11-14 13:02:13",
                "UninstallTime": "",
                "UninstallCmd": ""
            },
            {
                "HostIP": "172.23.0.36",
                "InstanceID": "ins-g4l64238",
                "Uuid": "c90117e5-6609-4ad6-b347-7a601dbb81f6",
                "OfflineTime": "2022-11-14 12:48:59",
                "UninstallTime": "",
                "UninstallCmd": ""
            }
        ],
        "RequestId": "74275f9f-9045-472a-8103-99027a2f87ba",
        "TotalCount": 945
    }
}
```

