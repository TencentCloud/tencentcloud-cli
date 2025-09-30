**Example 1: 创建水印模板**



Input: 

```
tccli mps CreateWatermarkTemplate --cli-unfold-argument  \
    --Name 水印模板1 \
    --Comment svg水印 \
    --Type svg \
    --CoordinateOrigin TopRight \
    --XPos 5% \
    --YPos 5% \
    --ImageTemplate.ImageContent  \
    --ImageTemplate.Width 10% \
    --ImageTemplate.Height 0px \
    --ImageTemplate.RepeatType once \
    --TextTemplate.FontType arial.ttf \
    --TextTemplate.FontSize 10px \
    --TextTemplate.FontColor #ffffff \
    --TextTemplate.FontAlpha 0.5 \
    --SvgTemplate.Width 10% \
    --SvgTemplate.Height 0px
```

Output: 
```
{
    "Response": {
        "Definition": 123,
        "ImageUrl": "",
        "RequestId": "93dda61a-c2c5-465d-a78c-0860997fb01b"
    }
}
```

