**Example 1: 按坐标签署合同**

按坐标签署合同

Input: 

```
tccli ds SignContractByCoordinate --cli-unfold-argument  \
    --Module ContractMng \
    --Operation SignContractByCoordinate \
    --ContractResId dcc-480rzey2gw \
    --AccountResId dcu-c33uil3apq \
    --AuthorizationTime 20180531142255 \
    --Position 10.0.0.238 \
    --SealResId dcs-c654e84rqw \
    --SignLocations.0.SignOnPage 1 \
    --SignLocations.0.SignLocationLBX 50 \
    --SignLocations.0.SignLocationLBY 140 \
    --SignLocations.0.SignLocationRUX 110 \
    --SignLocations.0.SignLocationRUY 200
```

Output: 
```
{
    "Response": {
        "RequestId": "c2dfb7d4-4d3a-4e3b-81eb-516bc06c29e6"
    }
}
```

