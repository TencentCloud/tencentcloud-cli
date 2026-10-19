**Example 1: MCP-APP工具调用**



Input: 

```
tccli adp CallMCPTool --cli-unfold-argument  \
    --PluginId 418eee0b-4aa7-4aef-939b-3c48d404e846 \
    --ThreadId 73251347-32c8-49a1-bea5-32a6aeb82ebc \
    --ToolName overtime_view_state \
    --Arguments {"viewUUID":"72e8f6a9-d87f-4067-b917-b5c7de90154f"}
```

Output: 
```
{
    "Response": {
        "Result": "{\"content\":[{\"type\":\"text\",\"text\":\"此表单尚未提交。\"}],\"structuredContent\":{\"submitted\":false}}",
        "RequestId": "8540d0bc-ed10-4c72-b04a-4bd441917434"
    }
}
```

