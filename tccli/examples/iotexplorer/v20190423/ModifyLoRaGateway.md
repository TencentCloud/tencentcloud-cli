**Example 1: 修改 LoRa 网关信息**



Input: 

```
tccli iotexplorer ModifyLoRaGateway --cli-unfold-argument  \
    --Description fortest3 \
    --IsPublic false \
    --Position tfine \
    --PositionDetails fyd \
    --GatewayId ff00000000000003 \
    --Location.Accuracy 0 \
    --Location.Altitude 1 \
    --Location.Latitude 120 \
    --Location.Longitude 113.44 \
    --Name gw3
```

Output: 
```
{
    "Response": {
        "Gateway": {
            "GatewayId": "ff00000000000003",
            "IsPublic": false,
            "Description": "fortest3",
            "Name": "gw3",
            "Position": "",
            "PositionDetails": "",
            "Location": {
                "Latitude": 0,
                "Longitude": 0,
                "Altitude": 0,
                "Accuracy": 0
            },
            "UpdatedAt": "2019-12-20 02:55:43 PM",
            "CreatedAt": "2019-12-05 03:53:32 PM",
            "LastSeenAt": ""
        },
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e"
    }
}
```

