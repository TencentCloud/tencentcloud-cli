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
        "RequestId": "xx"
    }
}
```

