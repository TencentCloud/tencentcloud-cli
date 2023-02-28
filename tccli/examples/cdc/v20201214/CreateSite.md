**Example 1: 创建站点**

创建站点

Input: 

```
tccli cdc CreateSite --cli-unfold-argument  \
    --Name my-site \
    --Description firstsite \
    --Note newsite \
    --FiberType MM \
    --OpticalStandard 1000Base-SX \
    --PowerConnectors 2 \
    --PowerFeedDrop above \
    --MaxWeight 500 \
    --PowerDrawKva 3000 \
    --UplinkSpeedGbps 10 \
    --UplinkCount 2 \
    --ConditionRequirement True \
    --DimensionRequirement True \
    --RedundantNetworking True \
    --Country China \
    --Province Guangdong \
    --City Shenzhen \
    --PostalCode 51800 \
    --AddressLine nanshan \
    --OptionalAddressLine tengda \
    --BreakerRequirement True \
    --RedundantPower True \
    --NeedHelp True
```

Output: 
```
{
    "Response": {
        "SiteId": "site-c738dj",
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc16"
    }
}
```

