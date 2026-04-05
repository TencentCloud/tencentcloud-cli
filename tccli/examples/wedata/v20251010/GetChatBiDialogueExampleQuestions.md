**Example 1: 获取对话过程中实例问题**



Input: 

```
tccli wedata GetChatBiDialogueExampleQuestions --cli-unfold-argument  \
    --WorkspaceId 17625100163628872 \
    --RoomKey 0ffb9e03da2045331767149632627887db30d35aa8d57 \
    --TaskKey 5565c5bcd5ff41a91767235282736b30ce042da24a74c \
    --DialogueKey b992c5ba73924f67176723528274892ee2be6bfb7194f
```

Output: 
```
{
    "Response": {
        "Data": {
            "AiGenerateItems": [
                "What is the sales revenue for potato chips?"
            ],
            "CanRefresh": true,
            "Items": [],
            "SystemConfigItems": [],
            "UserConfigItems": []
        },
        "RequestId": "d913d6ce-155e-4444-b9ab-7eec7e5c3e6f"
    }
}
```

