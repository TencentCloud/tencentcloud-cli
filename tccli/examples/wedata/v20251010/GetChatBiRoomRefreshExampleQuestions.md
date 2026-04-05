**Example 1: 首页实例问题换一换**



Input: 

```
tccli wedata GetChatBiRoomRefreshExampleQuestions --cli-unfold-argument  \
    --WorkspaceId 17625100163628872 \
    --RoomKey 0ffb9e03da2045331767149632627887db30d35aa8d57
```

Output: 
```
{
    "Response": {
        "Data": {
            "AiGenerateItems": [
                "What is the total gross profit for the entire period?"
            ],
            "CanRefresh": true,
            "Items": [],
            "SystemConfigItems": [
                "What tables are there and how are they connected? Give me a short summary."
            ],
            "UserConfigItems": [
                "哪种产品销售额最高？"
            ]
        },
        "RequestId": "79396959-58ba-493b-8622-0645a57fdf28"
    }
}
```

