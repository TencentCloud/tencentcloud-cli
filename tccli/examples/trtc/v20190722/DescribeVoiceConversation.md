**Example 1: 查询对话任务**



Input: 

```
tccli trtc DescribeVoiceConversation --cli-unfold-argument  \
    --SdkAppId 1400000311 \
    --TaskId -nG0jIFU7rPr0tFW0cg282rOxP*************************bUA9JbOXgp3tnRyVJAzlBFAE. \
    --DescribeType 1
```

Output: 
```
{
    "Response": {
        "HistoryContents": [
            {
                "Role": "user",
                "Content": "最近上海天气怎么样"
            },
            {
                "Role": "assistant",
                "Content": "我无法获取实时天气数据，所以没法告诉你上海当前的具体天气情况。建议你打开手机自带的天气应用，或访问中国天气网等平台查询最新预报。\n\n如果你告诉我具体日期，我也可以帮你说明上海这个季节通常的气候特点（比如气温范围、降水情况），供你参考。"
            }
        ],
        "StartTime": 1790081311564,
        "Status": "InProgress",
        "TaskId": "-nG0jIFU7rPr0tFW0cg282rOxP*************************bUA9JbOXgp3tnRyVJAzlBFAE.",
        "RequestId": "ebb2213e-7322-4f9b-8fcd-60c08a5168b7"
    }
}
```

