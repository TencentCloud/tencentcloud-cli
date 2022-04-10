**Example 1: 获取 LoRa 社区网关列表**



Input: 

```
tccli iotexplorer GetLoRaGatewayList --cli-unfold-argument  \
    --IsCommunity true
```

Output: 
```
{
    "Response": {
        "Gateways": [
            {
                "GatewayId": "ff00000000000003",
                "IsPublic": true,
                "Description": "fortest",
                "Name": "ddgw3",
                "Position": "tfine",
                "PositionDetails": "fyd",
                "Location": {
                    "Latitude": 0,
                    "Longitude": 0,
                    "Altitude": 0,
                    "Accuracy": 0
                },
                "UpdatedAt": "2019-12-05 03:53:32 PM",
                "CreatedAt": "2019-12-05 03:53:32 PM",
                "LastSeenAt": ""
            },
            {
                "GatewayId": "1000000000000019",
                "IsPublic": true,
                "Description": "fortest",
                "Name": "test0233",
                "Position": "tfine",
                "PositionDetails": "teshu",
                "Location": {
                    "Latitude": 0,
                    "Longitude": 0,
                    "Altitude": 0,
                    "Accuracy": 0
                },
                "UpdatedAt": "1970-01-01 08:00:00 AM",
                "CreatedAt": "2019-12-03 02:32:18 PM",
                "LastSeenAt": ""
            }
        ],
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e",
        "Total": 2
    }
}
```

**Example 2: 获取非社区网关列表**



Input: 

```
tccli iotexplorer GetLoRaGatewayList --cli-unfold-argument  \
    --Limit 1 \
    --IsCommunity True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Gateways": [
            {
                "GatewayId": "ff00000000000003",
                "IsPublic": true,
                "Description": "fortest",
                "Name": "ddgw3",
                "Position": "tfine",
                "PositionDetails": "fyd",
                "Location": {
                    "Latitude": 0,
                    "Longitude": 0,
                    "Altitude": 0,
                    "Accuracy": 0
                },
                "UpdatedAt": "2019-12-05 03:53:32 PM",
                "CreatedAt": "2019-12-05 03:53:32 PM",
                "LastSeenAt": ""
            },
            {
                "GatewayId": "ff00000000000004",
                "IsPublic": false,
                "Description": "fortest",
                "Name": "ddgw4",
                "Position": "",
                "PositionDetails": "",
                "Location": {
                    "Latitude": 0,
                    "Longitude": 0,
                    "Altitude": 0,
                    "Accuracy": 0
                },
                "UpdatedAt": "2019-12-05 04:13:50 PM",
                "CreatedAt": "2019-12-05 04:13:50 PM",
                "LastSeenAt": ""
            }
        ],
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e",
        "Total": 2
    }
}
```

