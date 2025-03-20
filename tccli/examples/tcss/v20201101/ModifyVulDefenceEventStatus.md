**Example 1: 修改漏洞防御事件状态**



Input: 

```
tccli tcss ModifyVulDefenceEventStatus --cli-unfold-argument  \
    --Status EVENT_DEALED \
    --EventIDs 1 \
    --Remark remark content
```

Output: 
```
{
    "Response": {
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a"
    }
}
```

