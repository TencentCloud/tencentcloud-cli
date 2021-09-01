**Example 1: 新建 LoRa 网关**



Input: 

```
tccli iotexplorer CreateLoRaGateway --cli-unfold-argument  \
    --Description fortest \
    --IsPublic true \
    --Position tfine \
    --PositionDetails fyd \
    --GatewayId ff00000000000002 \
    --Location.Accuracy 0 \
    --Location.Altitude 0 \
    --Location.Latitude 0 \
    --Location.Longitude 0 \
    --Name ddgws
```

Output: 
```
{
    "Response": {
        "Gateway": {
            "GatewayId": "ff00000000000005",
            "IsPublic": false,
            "Description": "fortest",
            "Name": "ddgw5",
            "Position": "",
            "PositionDetails": "",
            "Location": {
                "Latitude": 0,
                "Longitude": 0,
                "Altitude": 0,
                "Accuracy": 0
            },
            "UpdatedAt": "2019-12-05 05:03:02 PM",
            "CreatedAt": "2019-12-05 05:03:02 PM",
            "LastSeenAt": ""
        },
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e"
    }
}
```

