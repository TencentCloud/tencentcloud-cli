**Example 1: 修改资源调度中队列信息**



Input: 

```
tccli emr ModifyYarnQueueV2 --cli-unfold-argument  \
    --ConfigModifyInfoList.0.BasicParams.Items.0.Key state \
    --ConfigModifyInfoList.0.BasicParams.Items.0.Value RUNNING \
    --ConfigModifyInfoList.0.BasicParams.Items.1.Key default-node-label-expression \
    --ConfigModifyInfoList.0.BasicParams.Items.1.Value test \
    --ConfigModifyInfoList.0.BasicParams.Items.2.Key acl_submit_applications \
    --ConfigModifyInfoList.0.BasicParams.Items.2.Value {"user":"*","group":"*"} \
    --ConfigModifyInfoList.0.BasicParams.Items.3.Key acl_administer_queue \
    --ConfigModifyInfoList.0.BasicParams.Items.3.Value {"user":"*","group":"*"} \
    --ConfigModifyInfoList.0.BasicParams.Items.4.Key maximum-allocation-mb \
    --ConfigModifyInfoList.0.BasicParams.Items.4.Value 1024 \
    --ConfigModifyInfoList.0.BasicParams.Items.5.Key maximum-allocation-vcores \
    --ConfigModifyInfoList.0.BasicParams.Items.5.Value 2 \
    --ConfigModifyInfoList.0.ConfigSetParams.0.BasicParams.0.Key minimum-user-limit-percent \
    --ConfigModifyInfoList.0.ConfigSetParams.0.BasicParams.0.Value 1 \
    --ConfigModifyInfoList.0.ConfigSetParams.0.BasicParams.1.Key user-limit-factor \
    --ConfigModifyInfoList.0.ConfigSetParams.0.BasicParams.1.Value 1 \
    --ConfigModifyInfoList.0.ConfigSetParams.0.BasicParams.2.Key maximum-applications \
    --ConfigModifyInfoList.0.ConfigSetParams.0.BasicParams.2.Value 1000 \
    --ConfigModifyInfoList.0.ConfigSetParams.0.BasicParams.3.Key maximum-am-resource-percent \
    --ConfigModifyInfoList.0.ConfigSetParams.0.BasicParams.3.Value 0.005 \
    --ConfigModifyInfoList.0.ConfigSetParams.0.BasicParams.4.Key default-application-priority \
    --ConfigModifyInfoList.0.ConfigSetParams.0.BasicParams.4.Value 1 \
    --ConfigModifyInfoList.0.ConfigSetParams.0.ConfigSet default \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.0.Items.0.Key labelName \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.0.Items.0.Value <DEFAULT_PARTITION> \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.0.Items.1.Key capacity \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.0.Items.1.Value 100 \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.0.Items.2.Key maximum-capacity \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.0.Items.2.Value 100 \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.1.Items.0.Key labelName \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.1.Items.0.Value test \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.1.Items.1.Key capacity \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.1.Items.1.Value 100 \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.1.Items.2.Key maximum-capacity \
    --ConfigModifyInfoList.0.ConfigSetParams.0.LabelParams.1.Items.2.Value 100 \
    --ConfigModifyInfoList.0.MyId  \
    --ConfigModifyInfoList.0.Name test3 \
    --ConfigModifyInfoList.0.OpType 0 \
    --ConfigModifyInfoList.0.ParentId  \
    --InstanceId emr-324bjb6v \
    --Scheduler capacity
```

Output: 
```
{
    "Response": {
        "RequestId": "5419075a-9601-44a9-b045-a88561990ac0"
    }
}
```

