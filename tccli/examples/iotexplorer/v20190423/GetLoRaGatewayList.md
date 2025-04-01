**Example 1: 获取非社区网关列表**



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
                "FrequencyId": "freqId",
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
            }
        ],
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e",
        "Total": 1
    }
}
```

**Example 2: 获取 LoRa 社区网关列表**



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
                "FrequencyId": "freqId",
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
            }
        ],
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e",
        "Total": 2
    }
}
```

