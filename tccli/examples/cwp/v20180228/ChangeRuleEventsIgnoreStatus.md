**Example 1: 修改事件忽略状态接口**

根据检测项id或事件id进行批量忽略操作

Input: 

```
tccli cwp ChangeRuleEventsIgnoreStatus --cli-unfold-argument  \
    --IgnoreStatus 1 \
    --EventIdList 1 \
    --RuleIdList 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

