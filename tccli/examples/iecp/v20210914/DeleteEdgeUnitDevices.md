**Example 1: DeleteEdgeUnitDevices**



Input: 

```
tccli iecp DeleteEdgeUnitDevices --cli-unfold-argument  \
    --EdgeUnitId 100067 \
    --Devices.0.DeviceName link02 \
    --Devices.0.ProductId SA4RZ3NLIM
```

Output: 
```
{
    "Response": {
        "RequestId": "6aa02c8e-6f5f-4b7d-819a-4d1ef1ad210f"
    }
}
```

