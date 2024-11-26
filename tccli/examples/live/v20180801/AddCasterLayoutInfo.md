**Example 1: 添加布局20，绑定输入1，输入2**



Input: 

```
tccli live AddCasterLayoutInfo --cli-unfold-argument  \
    --LayoutInfo.LayoutIndex 1 \
    --LayoutInfo.InputIndexList 1|2 \
    --LayoutInfo.LayoutTemplateId 20 \
    --CasterId 1234
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

