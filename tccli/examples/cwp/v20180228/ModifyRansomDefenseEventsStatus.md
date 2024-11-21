**Example 1: 修改防勒索事件状态**

修改防勒索事件状态

Input: 

```
tccli cwp ModifyRansomDefenseEventsStatus --cli-unfold-argument  \
    --Status 1 \
    --Ids 1
```

Output: 
```
{
    "Response": {
        "RequestId": "935e27b1-d675-4509-80bf-96fbf0764237"
    }
}
```

