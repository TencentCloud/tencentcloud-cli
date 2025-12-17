**Example 1: CreateTCCatalogEndpoint示例**



Input: 

```
tccli tccatalog CreateTCCatalogEndpoint --cli-unfold-argument  \
    --VpcId vpc-1fsfes3 \
    --SubnetId subnet-1skewe
```

Output: 
```
{
    "Response": {
        "EndpointId": "1fsfes3",
        "Vip": "10.0.0.1",
        "RequestId": "83882c87-6a4c-47d5-9e4a-f32cd4c473ed"
    }
}
```

