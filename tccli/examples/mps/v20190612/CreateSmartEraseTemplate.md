**Example 1: 创建同时具有自动擦除和区域擦除能力的擦除字幕模板**

创建具有对预设区域检测文本并擦除，同时对指定时间段内指定区域直接擦除能力的擦除字幕模板

Input: 

```
tccli mps CreateSmartEraseTemplate --cli-unfold-argument  \
    --Name 擦除字幕模板2 \
    --EraseType subtitle \
    --EraseSubtitleConfig.SubtitleEraseMethod auto \
    --EraseSubtitleConfig.SubtitleModel standard \
    --EraseSubtitleConfig.CustomAreas.0.BeginMs 200 \
    --EraseSubtitleConfig.CustomAreas.0.EndMs 3000 \
    --EraseSubtitleConfig.CustomAreas.0.Areas.0.LeftTopX 0.05 \
    --EraseSubtitleConfig.CustomAreas.0.Areas.0.LeftTopY 0.1 \
    --EraseSubtitleConfig.CustomAreas.0.Areas.0.RightBottomX 0.75 \
    --EraseSubtitleConfig.CustomAreas.0.Areas.0.RightBottomY 0.9 \
    --EraseSubtitleConfig.CustomAreas.0.Areas.0.Unit 1
```

Output: 
```
{
    "Response": {
        "Definition": 200410,
        "RequestId": "835f2ecd-8666-4717-998b-02680437a8ef"
    }
}
```

**Example 2: 创建带有提取和翻译功能的擦除字幕模板**

创建带有提取和翻译功能的擦除字幕模板

Input: 

```
tccli mps CreateSmartEraseTemplate --cli-unfold-argument  \
    --Name 擦除字幕模板2 \
    --EraseType subtitle \
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
        "Definition": 200409,
        "RequestId": "ac14b422-1c7b-407d-9b95-530f1eea063d"
    }
}
```

