**Example 1: 创建规则**



Input: 

```
tccli cfw CreateAcRules --cli-unfold-argument  \
    --Data.0.OrderIndex 17 \
    --Data.0.SourceIp 0.0.0.0/0 \
    --Data.0.TargetIp 0.0.0.0/0 \
    --Data.0.Protocol TCP \
    --Data.0.Port -1/-1 \
    --Data.0.Strategy 0 \
    --Data.0.Detail andy创建的规则 \
    --Data.0.CloudCode 1 \
    --Data.0.SourceType 1 \
    --Data.0.TargetType 1 \
    --Data.0.Direction 1 \
    --Data.0.IsRegion 0 \
    --Data.0.Country 0 \
    --Data.0.City 0 \
    --Data.0.CityName chongqing \
    --Data.0.CountryName cn \
    --Type 0 \
    --EdgeId cfw-indf01efd \
    --InstanceId ins-ifndf00e \
    --Area ap-chongqing \
    --Enable 1
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Info": "success",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

