**Example 1: 修改模板20的布局使用的布局为输入2，输入3**



Input: 

```
tccli live ModifyCasterLayoutInfo --cli-unfold-argument  \
    --LayoutInfo.LayoutIndex 1 \
    --LayoutInfo.InputIndexList 2|3 \
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

