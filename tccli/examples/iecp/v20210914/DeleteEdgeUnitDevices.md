**Example 1: DeleteEdgeUnitDevices**



Input: 

```
tccli iecp DeleteEdgeUnitDevices --cli-unfold-argument  \
    --EdgeUnitId 0 \
    --Devices.0.DeviceName xx \
    --Devices.0.ProductId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

