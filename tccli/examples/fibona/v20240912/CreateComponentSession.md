**Example 1: 成功创建示例**

成功创建一个组件会话示例

Input: 

```
tccli fibona CreateComponentSession --cli-unfold-argument  \
    --UserGroupUniqueID rum-qZsJlN6****5QJEO** \
    --FAPPID e945370e2b3ee2ec \
    --TriggerID 12
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "SessionID": 233,
            "SessionTitle": "session_1ae2c15d-5dd3-456c-ab44-603d523d059c"
        },
        "Msg": "success",
        "RequestId": "70d4a798-7fcd-4603-908c-484226526da6"
    }
}
```

