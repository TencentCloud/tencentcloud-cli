**Example 1: 修改规则**



Input: 

```
tccli cfw ModifyAcRule --cli-unfold-argument  \
    --Data.0.OrderIndex 4 \
    --Data.0.Id 36064 \
    --Data.0.SourceIp 0.0.0.0/0 \
    --Data.0.TargetIp 0.0.0.0/0 \
    --Data.0.Protocol TCP \
    --Data.0.Port -1/-1 \
    --Data.0.Strategy 0 \
    --Data.0.Detail 333 \
    --Data.0.IsRegion 0 \
    --Data.0.Country 0 \
    --Data.0.City 0 \
    --Data.0.CloudCode  \
    --Data.0.SourceType 1 \
    --Data.0.TargetType 1 \
    --Data.0.Direction 1 \
    --Data.0.CityName  \
    --Data.0.CountryName  \
    --EdgeId  \
    --Enable 1 \
    --Area 
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Info": "",
        "RequestId": "5cdfff8d-bd3b-4411-91be-2117d4205f0f"
    }
}
```

