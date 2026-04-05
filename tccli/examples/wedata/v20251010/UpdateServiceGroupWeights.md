**Example 1: ServiceGroupWeights**



Input: 

```
tccli wedata UpdateServiceGroupWeights --cli-unfold-argument  \
    --WorkspaceId 1464962169590902784 \
    --ServiceGroupId 960ed2fc-f40e-4b34-b662-a3ed689e035b \
    --WeightEntries.0.ServiceId 960ed2fc-f40e-4b34-b662-a3ed689e035b-1 \
    --WeightEntries.0.Weight 50
```

Output: 
```
{
    "Response": {
        "Data": {
            "TiOneRequestId": "0b7c4c18-ad2b-4f5d-a25a-f337aaa42f7c"
        },
        "RequestId": "c18508a9-9878-467f-8152-2f524e531b2c"
    },
    "requestId": "3f39222e-b489-4c8b-a99f-c315a283122d"
}
```

