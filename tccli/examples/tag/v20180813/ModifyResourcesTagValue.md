**Example 1: Modifying tag value corresponding to tag key associated with multiple CVM instances in Guangzhou**



Input: 

```
tccli tag ModifyResourcesTagValue --cli-unfold-argument  \
    --ServiceType cvm\
    --ResourceRegion ap-guangzhou\
    --TagKey t1\
    --TagValue v1\
    --ResourcePrefix instance\
    --ResourceIds ins-001 ins-002
```

Output: 
```
{
    "Response": {
        "RequestId": "cc9a1529-edd3-4cf1-b2d1-4cd0ee2708cb"
    }
}
```

