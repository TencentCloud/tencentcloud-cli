**Example 1: 音频评估结果详情查询**

查询通过AudioSubmit接口提交的音频评估任务的结果。

Input: 

```
tccli tci DescribeConversationTask --cli-unfold-argument  \
    --JobId 101
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "JobId": 101,
        "Texts": [
            {
                "TextItem": {
                    "Mbtm": 810,
                    "Metm": 6880,
                    "Text": "I see a garage a helicopter a jellyfish a lizard and a napkin. ",
                    "TextSize": 63,
                    "Confidence": 4.5611e-41,
                    "Tag": 48,
                    "Words": [
                        {
                            "Mbtm": 1000,
                            "Metm": 1220,
                            "Text": "i",
                            "Wsize": 1,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 1220,
                            "Metm": 1440,
                            "Text": "see",
                            "Wsize": 3,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 1440,
                            "Metm": 1540,
                            "Text": "a",
                            "Wsize": 1,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 1540,
                            "Metm": 2080,
                            "Text": "garage",
                            "Wsize": 6,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 2120,
                            "Metm": 2240,
                            "Text": "a",
                            "Wsize": 1,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 2240,
                            "Metm": 3260,
                            "Text": "helicopter",
                            "Wsize": 10,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 3290,
                            "Metm": 3440,
                            "Text": "a",
                            "Wsize": 1,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 3440,
                            "Metm": 4380,
                            "Text": "jellyfish",
                            "Wsize": 9,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 4410,
                            "Metm": 4610,
                            "Text": "a",
                            "Wsize": 1,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 4610,
                            "Metm": 5180,
                            "Text": "lizard",
                            "Wsize": 6,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 5300,
                            "Metm": 5570,
                            "Text": "and",
                            "Wsize": 3,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 5570,
                            "Metm": 5740,
                            "Text": "a",
                            "Wsize": 1,
                            "Confidence": 0
                        },
                        {
                            "Mbtm": 5740,
                            "Metm": 6340,
                            "Text": "napkin",
                            "Wsize": 6,
                            "Confidence": 0
                        }
                    ]
                },
                "Speed": 2.1416805
            }
        ],
        "AsrStat": {
            "TotalDuration": 7580,
            "SoundDuration": 6070,
            "MuteDuration": 1510,
            "VadNum": 1,
            "WordNum": 13,
            "AvgSpeed": 2.1416805
        },
        "VocabAnalysisDetailInfo": null,
        "VocabAnalysisStatInfo": [
            {
                "VocabLibName": "praise",
                "VocabDetailInfo": null
            }
        ],
        "RequestId": "c3bf143a-a7cf-4651-baec-e291c62507dc",
        "Process": 0
    }
}
```

