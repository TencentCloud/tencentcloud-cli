**Example 1: 修改YARN资源调度的全局配置**



Input: 

```
tccli emr ModifyGlobalConfig --cli-unfold-argument  \
    --InstanceId emr-123 \
    --Items.0.Key enableResourceSchedule \
    --Items.0.Value true
```

Output: 
```
{
    "Response": {
        "RequestId": "514a7860-f50f-49ec-92eb-6d4558ec45c3"
    }
}
```

