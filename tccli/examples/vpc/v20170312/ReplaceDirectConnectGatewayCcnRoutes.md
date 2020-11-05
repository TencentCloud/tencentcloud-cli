**Example 1: Replacing the CCN routes of a Direct Connect gateway**



Input: 

```
tccli vpc ReplaceDirectConnectGatewayCcnRoutes --cli-unfold-argument  \
    --DirectConnectGatewayId dcg-prpqlmg1\
    --Routes.0.RouteId ccnr-bvipc87w\
    --Routes.0.DestinationCidrBlock 10.2.2.0/24\
    --Routes.1.RouteId ccnr-oc61so0o\
    --Routes.1.DestinationCidrBlock 10.2.3.0/24
```

Output: 
```
{
    "Response": {
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

