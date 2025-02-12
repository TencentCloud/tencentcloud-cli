**Example 1: 文件CA加签--同步模式**

文件CA加签--同步模式

Input: 

```
tccli ess CreateFileCounterSign --cli-unfold-argument  \
    --Operator.UserId yDCpyUc*******************bsVny9l \
    --SyncMode True \
    --FileId yDtwuU*******************FYPZ
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxxxxx",
        "ResultFileId": "yD45ww**********************ZIM1o",
        "Status": "FINISHED",
        "TaskId": "yDsdsU********************EtgCQI7"
    }
}
```

**Example 2: 文件CA加签--异步模式**

文件CA加签--异步模式

Input: 

```
tccli ess CreateFileCounterSign --cli-unfold-argument  \
    --Operator.UserId yDCpyUc*******************bsVny9l \
    --SyncMode True \
    --FileId yDtwuU*******************FYPZ
```

Output: 
```
{
    "Response": {
        "RequestId": "谢谢谢谢谢谢休息休息",
        "ResultFileId": "",
        "Status": "FINISHED",
        "TaskId": "yDtww************************EtgCQI7"
    }
}
```

**Example 3: 文件CA加签--同步模式--主带子场景**

文件CA加签，使用同步模式，且集团主企业使用子企业CA进行加签场景

Input: 

```
tccli ess CreateFileCounterSign --cli-unfold-argument  \
    --Operator.UserId yDCpyUc*******************bsVny9l \
    --Agent.ProxyOrganizationId yUIdyeU*******************bsdf234l \
    --SyncMode True \
    --FileId yDtwuU*******************FYPZ
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxxxxx",
        "ResultFileId": "yD45ww**********************ZIM1o",
        "Status": "FINISHED",
        "TaskId": "yDsdsU********************EtgCQI7"
    }
}
```

