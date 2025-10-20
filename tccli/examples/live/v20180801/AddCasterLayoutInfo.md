**Example 1: 添加布局20，绑定输入1，输入2**



Input: 

```
tccli live AddCasterLayoutInfo --cli-unfold-argument  \
    --LayoutInfo.LayoutIndex 1 \
    --LayoutInfo.InputIndexList 1|2 \
    --LayoutInfo.LayoutTemplateId 20 \
    --CasterId 63501
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 增加虚拟背景布局**

示例中，代表将输入2进行AI抠图，输入1作为输入2AI抠图后的叠加背景

Input: 

```
tccli live AddCasterLayoutInfo --cli-unfold-argument  \
    --CasterId 63501 \
    --LayoutInfo.InputIndexList 1|2 \
    --LayoutInfo.LayoutIndex 6 \
    --LayoutInfo.LayoutParams.0.LayerHeight 1 \
    --LayoutInfo.LayoutParams.0.LayerId 1 \
    --LayoutInfo.LayoutParams.0.LayerLocationX 0 \
    --LayoutInfo.LayoutParams.0.LayerLocationY 0 \
    --LayoutInfo.LayoutParams.0.LayerWidth 1 \
    --LayoutInfo.LayoutParams.0.UsePortraitSegment False \
    --LayoutInfo.LayoutParams.1.LayerHeight 0.5 \
    --LayoutInfo.LayoutParams.1.LayerId 2 \
    --LayoutInfo.LayoutParams.1.LayerLocationX 0.5 \
    --LayoutInfo.LayoutParams.1.LayerLocationY 0.5 \
    --LayoutInfo.LayoutParams.1.LayerWidth 0.5 \
    --LayoutInfo.LayoutParams.1.UsePortraitSegment True
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

