**Example 1: 修改资源调度中队列信息**



Input: 

```
tccli emr ModifyYarnQueueV2 --cli-unfold-argument  \
    --ConfigModifyInfoList.0.ConfigSetParams.0.ConfigSet default \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.0.Items.0.Key labelName \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.0.Items.0.Value <DEFAULT_PARTITION> \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.0.Items.1.Key capacity \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.0.Items.1.Value 50.0 \
    --ConfigModifyInfoList.0.MyId root.QPlt \
    --ConfigModifyInfoList.0.OpType 6 \
    --ConfigModifyInfoList.1.ConfigSetParams.0.ConfigSet default \
    --ConfigModifyInfoList.1.ConfigSetParams.0.LabelParams.0.Items.0.Key labelName \
    --ConfigModifyInfoList.1.ConfigSetParams.0.LabelParams.0.Items.0.Value <DEFAULT_PARTITION> \
    --ConfigModifyInfoList.1.ConfigSetParams.0.LabelParams.0.Items.1.Key capacity \
    --ConfigModifyInfoList.1.ConfigSetParams.0.LabelParams.0.Items.1.Value 50.0 \
    --ConfigModifyInfoList.1.MyId root.default \
    --ConfigModifyInfoList.1.OpType 6 \
    --InstanceId emr-h81 \
    --Scheduler capacity
```

Output: 
```
{
    "Response": {
        "RequestId": "2330fead-9b98-4bbc-a777-c9523ffb8e76"
    }
}
```

