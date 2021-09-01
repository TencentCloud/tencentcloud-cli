**Example 1: 按关键字签署合同**

按关键字签署合同

Input: 

```
tccli ds SignContractByKeyword --cli-unfold-argument  \
    --Module ContractMng \
    --Operation SignContractByKeyword \
    --ContractResId dcc-480rzey2gw \
    --AccountResId dcu-c33uil3apq \
    --AuthorizationTime 20180531142255 \
    --Position 10.0.0.238 \
    --SealResId dcs-c654e84rqw \
    --SignKeyword.Keyword (甲方) \
    --SignKeyword.OffsetCoordX 0 \
    --SignKeyword.OffsetCoordY 20 \
    --SignKeyword.ImageHeight 150 \
    --SignKeyword.ImageWidth 150
```

Output: 
```
{
    "Response": {
        "RequestId": "c2dfb7d4-4d3a-4e3b-81eb-516bc06c29e6"
    }
}
```

