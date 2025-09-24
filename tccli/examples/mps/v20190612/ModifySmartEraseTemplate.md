**Example 1: 修改擦除字幕模板打开提取功能**

修改擦除字幕模板，打开OCR提取以及翻译功能

Input: 

```
tccli mps ModifySmartEraseTemplate --cli-unfold-argument  \
    --Definition 200410 \
    --EraseSubtitleConfig.SubtitleEraseMethod auto \
    --EraseSubtitleConfig.SubtitleModel standard \
    --EraseSubtitleConfig.OcrSwitch ON \
    --EraseSubtitleConfig.SubtitleLang zh_en \
    --EraseSubtitleConfig.SubtitleFormat vtt \
    --EraseSubtitleConfig.TransSwitch ON \
    --EraseSubtitleConfig.TransDstLang en
```

Output: 
```
{
    "Response": {
        "RequestId": "84265f8e-43ec-4449-9521-b9332f64ee79"
    }
}
```

**Example 2: 修改擦除水印模板更改模型**

修改擦除水印模板，将擦除水印模型更改为高级版

Input: 

```
tccli mps ModifySmartEraseTemplate --cli-unfold-argument  \
    --Definition 200407 \
    --EraseWatermarkConfig.WatermarkEraseMethod auto \
    --EraseWatermarkConfig.WatermarkModel advanced
```

Output: 
```
{
    "Response": {
        "RequestId": "e4d526f3-f1bb-4030-9f0d-00df485a7eae"
    }
}
```

