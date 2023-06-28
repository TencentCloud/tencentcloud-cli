**Example 1: 请求示例**

复制组内只读实例设置为主实例

Input: 

```
tccli redis ChangeMasterInstance --cli-unfold-argument  \
    --InstanceId crs-sa5**** \
    --GroupId crs-rpl-sa5**** \
    --ForceSwitch False
```

Output: 
```
{
    "Response": {
        "TaskId": 327,
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522"
    }
}
```

