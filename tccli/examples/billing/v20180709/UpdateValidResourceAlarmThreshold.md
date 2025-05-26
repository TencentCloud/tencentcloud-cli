**Example 1: 停用余量预警配置示例**

客户级余量预警配置停用请求

Input: 

```
tccli billing UpdateValidResourceAlarmThreshold --cli-unfold-argument  \
    --ProductCode p_trade_t_s \
    --ThresholdType 4 \
    --ValidStatus 0 \
    --GroupId TestGroup
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": 0
        },
        "RequestId": "a6cb7a6e-9137-4112-8dcd-b51fd7e3b07f"
    }
}
```

**Example 2: 启用余量预警配置示例**

客户级余量预警配置启用请求

Input: 

```
tccli billing UpdateValidResourceAlarmThreshold --cli-unfold-argument  \
    --ProductCode p_trade_t_s \
    --ThresholdType 4 \
    --ValidStatus 1 \
    --GroupId TestGroup
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": 0
        },
        "RequestId": "a6cb7a6e-9137-4112-8dcd-b51fd7e3b07f"
    }
}
```

**Example 3: 启动/停用客户级配置时配置不存在**

当用户需要更新的预警配置不存在时返回错误

Input: 

```
tccli billing UpdateValidResourceAlarmThreshold --cli-unfold-argument  \
    --ProductCode p_trade_t_s \
    --ThresholdType 6 \
    --ValidStatus 0 \
    --GroupId TestGroup
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue",
            "Message": "not find db config"
        },
        "RequestId": "2dd5b7c5-2ecd-472c-95b9-4cb3488190d2"
    }
}
```

