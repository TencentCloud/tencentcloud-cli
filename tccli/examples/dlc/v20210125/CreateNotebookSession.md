**Example 1: 创建交互式session（notebook）**

创建交互式session（notebook）

Input: 

```
tccli dlc CreateNotebookSession --cli-unfold-argument  \
    --Name notebook_session_1 \
    --Kind spark \
    --DataEngineName engine1 \
    --DriverSize small \
    --ExecutorSize small \
    --ExecutorNumbers 1 \
    --ExecutorMaxNumbers 0 \
    --Arguments.0.Key dlc.role.arn \
    --Arguments.0.Value qcs::cam::uin/1**********1:roleName/role1 \
    --ProxyUser user1 \
    --TimeoutInSecond 3600 \
    --SparkImage  \
    --IsInherit 0
```

Output: 
```
{
    "Response": {
        "SessionId": "livy-session-*************",
        "SparkAppId": "",
        "State": "starting",
        "RequestId": "********-****-****-****-834e16ecf001"
    }
}
```

