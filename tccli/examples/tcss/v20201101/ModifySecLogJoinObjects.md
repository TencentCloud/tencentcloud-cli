**Example 1: 修改安全日志接入对象**

修改安全日志接入对象

Input: 

```
tccli tcss ModifySecLogJoinObjects --cli-unfold-argument  \
    --LogType container_bash \
    --BindList 3b6b1bbc-1c7a-47e2-9ca8-e9c27ec9d068 \
    --NodeType NORMAL \
    --RangeType 0 \
    --AutoJoin False
```

Output: 
```
{
    "Response": {
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

