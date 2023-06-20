**Example 1: 示例**

升级当前实例至Redis 4.0 集群架构

Input: 

```
tccli redis UpgradeInstanceVersion --cli-unfold-argument  \
    --InstanceId crs-5qlr**** \
    --SwitchOption 2 \
    --TargetInstanceType 7
```

Output: 
```
{
    "Response": {
        "DealId": "6954227",
        "RequestId": "4daddc97-0005-45d8-b5b8-38514ec1e97c"
    }
}
```

