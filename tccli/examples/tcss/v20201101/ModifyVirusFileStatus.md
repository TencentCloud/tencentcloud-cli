**Example 1: 运行时更新木马文件事件状态**



Input: 

```
tccli tcss ModifyVirusFileStatus --cli-unfold-argument  \
    --EventIdSet 12afdwasfdasfds \
    --Status EVENT_ADD_WHITE \
    --Remark 加白
```

Output: 
```
{
    "Response": {
        "RequestId": "safdswwasafd"
    }
}
```

