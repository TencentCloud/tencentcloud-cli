**Example 1: 无查询条件**

 

Input: 

```
tccli iss ListOrganizationChannels --cli-unfold-argument  \
    --OrganizationId 182 \
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
                    "ChannelId": "000fb77b-f309-****-****-d4aff5503d70",
                    "ChannelName": "dev_1",
                    "DeviceId": "81b14b2d-f309-****-****-3d1a3c3f630f",
                    "DeviceName": "gb-device11814",
                    "InPlan": true
                },
                {
                    "ChannelId": "0020a697-f309-****-****-c836d9f95075",
                    "ChannelName": "dev_1",
                    "DeviceId": "c94a9cc1-ee07-****-******-c87b6065893d",
                    "DeviceName": "gb-device11820",
                    "InPlan": true
                },
                {
                    "ChannelId": "002b99cb-f309-****-****-fb573cc57ab8",
                    "ChannelName": "dev_1",
                    "DeviceId": "a7718b36-f309-****-****-b417bd2aa809",
                    "DeviceName": "gb-device3633",
                    "InPlan": true
                },
                {
                    "ChannelId": "15daac41-f309-****-****-0cadab7a6256",
                    "ChannelName": "PTZ03",
                    "DeviceId": "cae2132a-7edc-****-****-19cc90a61f06",
                    "DeviceName": "NVR-04",
                    "InPlan": true
                },
                {
                    "ChannelId": "222c9da5-*18b3-****-****-107c013b95a7",
                    "ChannelName": "PTZ09",
                    "DeviceId": "389708b2-708b-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "InPlan": true
                }
            ],
            "PageNumber": 1,
            "PageSize": 5,
            "TotalCount": 13
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

**Example 2: 按照设备名称查询**

 

Input: 

```
tccli iss ListOrganizationChannels --cli-unfold-argument  \
    --OrganizationId 182 \
    --DeviceName abc \
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
                    "InPlan": true
                },
                {
                    "ChannelId": "32525dd7-c3fc-****-****-d5beb4acd1e1",
                    "ChannelName": "11",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "InPlan": true
                },
                {
                    "ChannelId": "53ca64d3-9627-****-****-cea5122f6977",
                    "ChannelName": "PTZ03",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "InPlan": true
                },
                {
                    "ChannelId": "c80a0ebf-10ac-****-****-8083f18df240",
                    "ChannelName": "PTZ17",
                    "DeviceId": "389708b2-bcbb-****-****-a61f528b2a15",
                    "DeviceName": "SDK-NVR05",
                    "InPlan": true
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

**Example 3: 按照通道名称查询**

 

Input: 

```
tccli iss ListOrganizationChannels --cli-unfold-argument  \
    --OrganizationId 182 \
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
                    "InPlan": true
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

