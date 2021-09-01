**Example 1: 修改DDoS的AI防护状态**



Input: 

```
tccli dayu ModifyDDoSAIStatus --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Method set \
    --DDoSAI on
```

Output: 
```
{
    "Response": {
        "DDoSAI": "on",
        "Id": "bgpip-000000xe",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

