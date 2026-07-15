**Example 1: 授权维修任务立即进行处理**

授权待授权的维修任务，允许立即进行处理

Input: 

```
tccli cvm RepairTaskControl --cli-unfold-argument  \
    --Product CVM \
    --InstanceIds ins-xxxxxxxx \
    --TaskId rep-xxxxxxxx \
    --Operate AuthorizeRepair
```

Output: 
```
{
    "Response": {
        "RequestId": "86a2683e-dabe-4c42-b6b7-e7a209428f41",
        "TaskId": "rep-xxxxxxxx"
    }
}
```

**Example 2: 预约维修任务在指定时间进行处理**

提前预约待授权的维修任务在`2023-01-02 12:00:00`授权进行处理

Input: 

```
tccli cvm RepairTaskControl --cli-unfold-argument  \
    --Product CVM \
    --InstanceIds ins-xxxxxxxx \
    --TaskId rep-xxxxxxxx \
    --Operate AuthorizeRepair \
    --OrderAuthTime 2023-01-02 12:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "86a2683e-dabe-4c42-b6b7-e7a209428f41",
        "TaskId": "rep-xxxxxxxx"
    }
}
```

