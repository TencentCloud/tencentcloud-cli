**Example 1: 获取资源调度中的队列信息**



Input: 

```
tccli emr DescribeYarnQueue --cli-unfold-argument  \
    --InstanceId emr-fa13 \
    --Scheduler capacity
```

Output: 
```
{
    "Response": {
        "Queue": "{\"name\":\"root\",\"myId\":\"root\",\"parentId\":\"root\",\"configs\":[{\"configName\":\"default\",\"labels\":[{\"labelName\":\"\\u003cDEFAULT_PARTITION\\u003e\",\"capacity\":null,\"maximum-capacity\":null,\"state\":0},{\"labelName\":\"test\",\"capacity\":null,\"maximum-capacity\":null,\"state\":0},{\"labelName\":\"test2\",\"capacity\":null,\"maximum-capacity\":null,\"state\":0}],\"minimum-user-limit-percent\":null,\"user-limit-factor\":null,\"maximum-applications\":null,\"maximum-am-resource-percent\":null,\"default-application-priority\":null}],\"state\":null,\"default-node-label-expression\":null,\"acl_submit_applications\":null,\"acl_administer_queue\":null,\"maximum-allocation-mb\":null,\"maximum-allocation-vcores\":null,\"isDefault\":null,\"isRoot\":true,\"queues\":[{\"name\":\"default\",\"myId\":\"root.default\",\"parentId\":\"root\",\"configs\":[{\"configName\":\"default\",\"labels\":[{\"labelName\":\"\\u003cDEFAULT_PARTITION\\u003e\",\"capacity\":50,\"maximum-capacity\":100,\"state\":0}],\"minimum-user-limit-percent\":null,\"user-limit-factor\":1,\"maximum-applications\":null,\"maximum-am-resource-percent\":null,\"default-application-priority\":null}],\"state\":null,\"default-node-label-expression\":null,\"acl_submit_applications\":null,\"acl_administer_queue\":null,\"maximum-allocation-mb\":null,\"maximum-allocation-vcores\":null,\"isDefault\":true,\"isRoot\":null,\"queues\":[]},{\"name\":\"q1\",\"myId\":\"root.q1\",\"parentId\":\"root\",\"configs\":[{\"configName\":\"default\",\"labels\":[{\"labelName\":\"\\u003cDEFAULT_PARTITION\\u003e\",\"capacity\":50,\"maximum-capacity\":100,\"state\":0},{\"labelName\":\"test\",\"capacity\":100,\"maximum-capacity\":100,\"state\":0}],\"minimum-user-limit-percent\":null,\"user-limit-factor\":null,\"maximum-applications\":null,\"maximum-am-resource-percent\":null,\"default-application-priority\":null}],\"state\":\"RUNNING\",\"default-node-label-expression\":null,\"acl_submit_applications\":{\"user\":\"*\",\"group\":\"*\"},\"acl_administer_queue\":{\"user\":\"*\",\"group\":\"*\"},\"maximum-allocation-mb\":null,\"maximum-allocation-vcores\":null,\"isDefault\":null,\"isRoot\":null,\"queues\":[]}]}",
        "Version": "v3",
        "RequestId": "3f63c907-d4e4-4856-b05d-949eedc2151a"
    }
}
```

