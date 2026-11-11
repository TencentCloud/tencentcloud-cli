**Example 1: 查询多模态理解任务**



Input: 

```
tccli mps DescribeModelChatTask --cli-unfold-argument  \
    --TaskId vlm-task-88bf381117a1b62ed7e7e5f47199dbb9
```

Output: 
```
{
    "Response": {
        "Choices": [
            {
                "FinishReason": "stop",
                "Index": 0,
                "Message": {
                    "Content": "这是一张走极简治愈路线的静物摄影作品，整体氛围舒缓恬淡，充满松弛的日常美学感：\n1. **基底与色调**：整张图用低饱和的暖调莫兰迪色系统一铺陈，占画面90%以上的区域都是带有极细微哑光肌理的浅奶杏色台面，搭配同色系更浅的米白背景，二者几乎无缝衔接，留出了极其充裕的空白区域，没有任何多余杂物干扰视觉。\n2. **视觉主体**：仅在画面偏左下角的位置放置了全部内容：两颗紧紧挨在一起的圆润新鲜蜜橘，橘子表皮是柔和的暖橘调哑光质感，带着柑橘皮特有的细微磨砂肌理，靠后的那只橘子顶部还留了一小截短短的鲜绿色果蒂，两只橘子底下压着两三片小巧舒展的嫩绿色柑橘叶，小面积的鲜亮绿和暖橘色互相衬得格外清爽。\n3. **光影与构图**：画面用的是非常匀净柔和的漫射自然光，没有生硬的明暗交界线，橘子在台面上投下边缘模糊、浅淡得几乎要融在底色里的软阴影，完全没有强烈明暗对比。采用偏重心的留白构图，主体安放在左下侧，大片空白给画面极强的呼吸感，整体传递出类似慵懒夏日午后的闲适安静感，视觉舒适度极高，是典型的极简生活类ins风美学画面，常被用作背景素材、治愈系壁纸。",
                    "Role": "assistant"
                }
            }
        ],
        "Created": 1793793238,
        "Id": "mps_********_r00c00_sensev1_900094c10430a82604ae220811145f5a",
        "Model": "wand-vega-vl-1.0-pro",
        "Msg": "success",
        "Object": "chat.completion",
        "TaskId": "vlm-task-88bf381117a1b62ed7e7e5f47199dbb9",
        "Usage": {
            "CompletionTokens": 1178,
            "PromptTokens": 6,
            "TotalTokens": 1184
        },
        "RequestId": "8bd257ae-b382-4a5d-884f-f8977996d754"
    }
}
```

