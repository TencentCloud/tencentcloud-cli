**Example 1: RecognizeAudio**



Input: 

```
tccli mps RecognizeAudio --cli-unfold-argument  \
    --Source zh \
    --AudioFormat pcm \
    --AudioData KwDn/zIA5v///wUA0v8D
```

Output: 
```
{
    "RequestId": "f27f3866-3882-4c18-a4ac-3b3d83fd2f5a",
    "Response": {
        "AudioLength": 4.2,
        "RequestId": "f27f3866-3882-4c18-a4ac-3b3d83fd2f5a",
        "Sentence": [
            {
                "End": 3.59,
                "Start": 0.03,
                "Text": "在人民大会堂举行第三次和第四次会议。",
                "WordsInfo": [
                    {
                        "End": 0.27,
                        "Start": 0.03,
                        "Word": "在"
                    },
                    {
                        "End": 0.43,
                        "Start": 0.27,
                        "Word": "人"
                    },
                    {
                        "End": 0.51,
                        "Start": 0.43,
                        "Word": "民"
                    },
                    {
                        "End": 0.71,
                        "Start": 0.51,
                        "Word": "大"
                    },
                    {
                        "End": 0.91,
                        "Start": 0.71,
                        "Word": "会"
                    },
                    {
                        "End": 1.07,
                        "Start": 0.91,
                        "Word": "堂"
                    },
                    {
                        "End": 1.55,
                        "Start": 1.39,
                        "Word": "举"
                    },
                    {
                        "End": 1.71,
                        "Start": 1.55,
                        "Word": "行"
                    },
                    {
                        "End": 1.95,
                        "Start": 1.75,
                        "Word": "第"
                    },
                    {
                        "End": 2.15,
                        "Start": 1.95,
                        "Word": "三"
                    },
                    {
                        "End": 2.39,
                        "Start": 2.15,
                        "Word": "次"
                    },
                    {
                        "End": 2.75,
                        "Start": 2.47,
                        "Word": "和"
                    },
                    {
                        "End": 2.91,
                        "Start": 2.75,
                        "Word": "第"
                    },
                    {
                        "End": 3.11,
                        "Start": 2.91,
                        "Word": "四"
                    },
                    {
                        "End": 3.27,
                        "Start": 3.11,
                        "Word": "次"
                    },
                    {
                        "End": 3.51,
                        "Start": 3.31,
                        "Word": "会"
                    },
                    {
                        "End": 3.59,
                        "Start": 3.51,
                        "Word": "议。"
                    }
                ]
            }
        ],
        "Text": "在人民大会堂举行第三次和第四次会议。"
    }
}
```

