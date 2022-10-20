**Example 1: 修改漏洞防御事件状态**



Input: 

```
tccli tcss ModifyVulDefenceEventStatus --cli-unfold-argument  \
    --Status EVENT_DEALED \
    --EventIDs 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

