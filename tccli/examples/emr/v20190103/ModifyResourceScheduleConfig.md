**Example 1: 修改yarn资源调度的资源配置**



Input: 

```
tccli emr ModifyResourceScheduleConfig --cli-unfold-argument  \
    --InstanceId emr-buy439fq \
    --Key capacity \
    --Value {"queueMappings":[{"mapping-type":"u","name":"1331","full-queue-name":"132","special-name":true,"special-queue":true}],"queue":{"name":"root","capacity":100,"maximum-capacity":100,"minimum-user-limit-percent":0,"user-limit-factor":0,"maximum-allocation-mb":0,"maximum-allocation-vcores":0,"state":null,"maximum-applications":0,"maximum-am-resource-percent":0,"acl_submit_applications":null,"acl_administer_queue":null,"queues":[{"name":"121","capacity":12,"maximum-capacity":12,"minimum-user-limit-percent":12,"user-limit-factor":12,"maximum-allocation-mb":12,"maximum-allocation-vcores":12,"state":"RUNNING","maximum-applications":10000,"maximum-am-resource-percent":25,"acl_submit_applications":{"user":"*","group":"*"},"acl_administer_queue":{"user":"*","group":"*"},"queues":null},{"name":"12","capacity":12,"maximum-capacity":12,"minimum-user-limit-percent":12,"user-limit-factor":12,"maximum-allocation-mb":12,"maximum-allocation-vcores":12,"state":"RUNNING","maximum-applications":10000,"maximum-am-resource-percent":25,"acl_submit_applications":{"user":"*","group":"*"},"acl_administer_queue":{"user":"*","group":"*"},"queues":null},{"name":"default","capacity":76,"maximum-capacity":100,"minimum-user-limit-percent":12,"user-limit-factor":1,"maximum-allocation-mb":12,"maximum-allocation-vcores":12,"state":"RUNNING","maximum-applications":12,"maximum-am-resource-percent":12,"acl_submit_applications":{"user":"*","group":"*"},"acl_administer_queue":{"user":"*","group":"*"},"queues":[{"name":"d1","capacity":100,"maximum-capacity":100,"minimum-user-limit-percent":null,"user-limit-factor":null,"maximum-allocation-mb":null,"maximum-allocation-vcores":null,"state":"RUNNING","maximum-applications":10000,"maximum-am-resource-percent":25,"acl_submit_applications":{"user":"*","group":"*"},"acl_administer_queue":{"user":"*","group":"*"},"queues":null}]}]},"queueMappingsOverride":true}
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "xx",
        "Data": "xx",
        "RequestId": "xx",
        "IsDraft": true
    }
}
```

