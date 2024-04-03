**Example 1: 无查询条件**

 

Input: 

```
tccli iss ListRecordPlanDevices --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "ChannelId": "000fb77b-****-****-****-d4aff5503d70",
                    "ChannelName": "dev_1",
                    "DeviceId": "81b14b2d-****-****-****-3d1a3c3f630f",
                    "DeviceName": "gb-device11814",
                    "OrganizationName": "组织1"
                },
                {
                    "ChannelId": "0020a697-****-****-****-c836d9f95075",
                    "ChannelName": "dev_1",
                    "DeviceId": "c94a9cc1-****-****-****-c87b6065893d",
                    "DeviceName": "gb-device11820",
                    "OrganizationName": "组织2"
                },
                {
                    "ChannelId": "002b99cb-****-****-****-fb573cc57ab8",
                    "ChannelName": "dev_1",
                    "DeviceId": "a7718b36-****-****-****-b417bd2aa809",
                    "DeviceName": "gb-device3633",
                    "OrganizationName": "组织2"
                },
                {
                    "ChannelId": "15daac41-****-****-****-0cadab7a6256",
                    "ChannelName": "PTZ03",
                    "DeviceId": "cae2132a-****-****-****-19cc90a61f06",
                    "DeviceName": "NVR-04",
                    "OrganizationName": "201"
                },
                {
                    "ChannelId": "222c9da5-****-****-****-107c013b95a7",
                    "ChannelName": "PTZ09",
                    "DeviceId": "389708b2-****-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "OrganizationName": "201"
                }
            ],
            "PageNumber": 1,
            "PageSize": 5,
            "TotalCount": 15
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

**Example 2: 按照组织名称查询**

 

Input: 

```
tccli iss ListRecordPlanDevices --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --OrganizationName 201 \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "ChannelId": "15daac41-f309-****-****-0cadab7a6256",
                    "ChannelName": "PTZ03",
                    "DeviceId": "cae2132a-7edc-****-****-19cc90a61f06",
                    "DeviceName": "NVR-04",
                    "OrganizationName": "201"
                },
                {
                    "ChannelId": "222c9da5-3e06-****-****-107c013b95a7",
                    "ChannelName": "DaHua-PTZ 09",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "OrganizationName": "201"
                },
                {
                    "ChannelId": "32525dd7-c3fc-****-****-d5beb4acd1e1",
                    "ChannelName": "11",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "OrganizationName": "201"
                },
                {
                    "ChannelId": "53ca64d3-9627-****-****-cea5122f6977",
                    "ChannelName": "PTZ03",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "OrganizationName": "201"
                },
                {
                    "ChannelId": "60a645e8-3140-****-****-98a62528232b",
                    "ChannelName": "IPDome",
                    "DeviceId": "3f6c847f-b6ea-****-****-2bfc8208d97e",
                    "DeviceName": "onvif03",
                    "OrganizationName": "201"
                }
            ],
            "PageNumber": 1,
            "PageSize": 5,
            "TotalCount": 12
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

**Example 3: 按照设备名称查询**

 

Input: 

```
tccli iss ListRecordPlanDevices --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --DeviceName NVR05 \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "ChannelId": "222c9da5-3e06-****-****-107c013b95a7",
                    "ChannelName": "PTZ09",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "OrganizationName": "201"
                },
                {
                    "ChannelId": "32525dd7-c3fc-****-****-d5beb4acd1e1",
                    "ChannelName": "11",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "OrganizationName": "201"
                },
                {
                    "ChannelId": "53ca64d3-9627-****-****-cea5122f6977",
                    "ChannelName": "PTZ03",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "OrganizationName": "201"
                },
                {
                    "ChannelId": "c80a0ebf-10ac-****-****-8083f18df240",
                    "ChannelName": "PTZ17",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "OrganizationName": "201"
                }
            ],
            "PageNumber": 1,
            "PageSize": 4,
            "TotalCount": 4
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

**Example 4: 按照通道名称查询**

 

Input: 

```
tccli iss ListRecordPlanDevices --cli-unfold-argument  \
    --PlanId 88ac5ea6c1f**********24671d0f94f \
    --ChannelName 11 \
    --PageSize 5 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "ChannelId": "32525dd7-c3fc-****-****-d5beb4acd1e1",
                    "ChannelName": "11",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "OrganizationName": "201"
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": 1
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

