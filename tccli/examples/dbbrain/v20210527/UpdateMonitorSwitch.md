**Example 1: 更新Agent实例状态**

更新Agent实例状态（停止或者重连实例）

Input: 

```
tccli dbbrain UpdateMonitorSwitch --cli-unfold-argument  \
    --Switch on \
    --InstanceId mysql-069yc1dda \
    --Product ap-chengdu
```

Output: 
```
{
    "Response": {
        "RequestId": "b49053b9-f21c-40ec-a1ce-d1a5fae5193f"
    }
}
```

