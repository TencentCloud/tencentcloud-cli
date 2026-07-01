**Example 1: request success**



Input: 

```
tccli dataagent ExecuteAgentApiV1 --cli-unfold-argument  \
    --RequestPath /api/teams/big-data-team/sessions/20260603_211035_cc30c0/chat/events \
    --RequestType event-stream
```

Output: 
```
{
    "index": 4,
    "delta": " SSE"
}
```

