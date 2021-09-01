**Example 1: 业务日志搜索**



Input: 

```
tccli tsf SearchBusinessLog --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --StartTime '2019-05-29 16:06:08' \
    --EndTime '2019-05-29 17:06:08' \
    --OrderBy score \
    --ConfigId apm-busi-log-cfg-6a7m36a5 \
    --GroupIds group-gvkqkdjv \
    --InstanceIds openapi-service-api-c594fd9cd-x76rf
```

Output: 
```
{
    "Response": {
        "RequestId": "01e72376-fdbd-4b96-ab81-6c04edce442e",
        "Result": {
            "TotalCount": 184,
            "Content": [
                {
                    "LogId": "AWsCop02uXjszoOzsHWG",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:08:54.072  INFO [openapi-service-api,3898e77614d63944,3898e77614d63944,true] 1 --- [http-nio-80-exec-2] c.k.t.o.service.api.aop.HttpAspect       : url=http://testprh.yunassess.com/push/getByOffset",
                    "Timestamp": 1559117334072
                },
                {
                    "LogId": "AWsCop02uXjszoOzsHWJ",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:08:54.072  INFO [openapi-service-api,3898e77614d63944,3898e77614d63944,true] 1 --- [http-nio-80-exec-2] c.k.t.o.service.api.aop.HttpAspect       : class_method=com.ke.txprh.openapi.service.api.controller.PushController.getOnyByOffset",
                    "Timestamp": 1559117334072
                },
                {
                    "LogId": "AWsCp3BR2hErXcJYbH4i",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:13:56.369  INFO [openapi-service-api,ce4fc5d9d17c042f,ce4fc5d9d17c042f,true] 1 --- [http-nio-80-exec-4] c.k.t.o.service.api.aop.HttpAspect       : 方法结束",
                    "Timestamp": 1559117636369
                },
                {
                    "LogId": "AWsCp0lBuXjszoOzscRb",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:13:56.359  INFO [openapi-service-api,ce4fc5d9d17c042f,ce4fc5d9d17c042f,true] 1 --- [http-nio-80-exec-4] c.k.t.o.service.api.aop.HttpAspect       : 方法环绕start.....",
                    "Timestamp": 1559117636359
                },
                {
                    "LogId": "AWsCp0lBuXjszoOzscRg",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:13:56.359  INFO [openapi-service-api,ce4fc5d9d17c042f,ce4fc5d9d17c042f,true] 1 --- [http-nio-80-exec-4] c.k.t.o.service.api.aop.HttpAspect       : get入参args=0",
                    "Timestamp": 1559117636359
                },
                {
                    "LogId": "AWsCqZOV2hErXcJYbUBX",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:16:19.751  INFO [openapi-service-api,e64eaaa959f51579,e64eaaa959f51579,true] 1 --- [pool-2-thread-1] o.s.c.t.r.sync.TsfRouteConsulKVLoader    : tsf route rule, routeRuleInfoMap: {}",
                    "Timestamp": 1559117779751
                },
                {
                    "LogId": "AWsCq8Z7uXjszoOzswqr",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:18:58.675  INFO [openapi-service-api,34a8a2e5d403a84e,34a8a2e5d403a84e,true] 1 --- [http-nio-80-exec-1] c.k.t.o.service.api.aop.HttpAspect       : url=http://testprh.yunassess.com/push/getByOffset",
                    "Timestamp": 1559117938675
                },
                {
                    "LogId": "AWsCq8Z7uXjszoOzswqu",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:18:58.675  INFO [openapi-service-api,34a8a2e5d403a84e,34a8a2e5d403a84e,true] 1 --- [http-nio-80-exec-1] c.k.t.o.service.api.aop.HttpAspect       : class_method=com.ke.txprh.openapi.service.api.controller.PushController.getOnyByOffset",
                    "Timestamp": 1559117938675
                },
                {
                    "LogId": "AWsCq8Z7uXjszoOzswq2",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:18:58.769  INFO [openapi-service-api,5b7d9126c385642d,5b7d9126c385642d,true] 1 --- [http-nio-80-exec-9] c.k.t.o.service.api.aop.HttpAspect       : class_method=com.ke.txprh.openapi.service.api.controller.PushController.getOnyByOffset",
                    "Timestamp": 1559117938769
                },
                {
                    "LogId": "AWsCq85M2hErXcJYbg7s",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:19:00.239  INFO [openapi-service-api,487dcec58abfc6ce,487dcec58abfc6ce,true] 1 --- [http-nio-80-exec-6] c.k.t.o.service.api.aop.HttpAspect       : url=http://testprh.yunassess.com/push/multiCallbackSendResult",
                    "Timestamp": 1559117940239
                },
                {
                    "LogId": "AWsCq85M2hErXcJYbg7t",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:19:00.240  INFO [openapi-service-api,487dcec58abfc6ce,487dcec58abfc6ce,true] 1 --- [http-nio-80-exec-6] c.k.t.o.service.api.aop.HttpAspect       : method=POST",
                    "Timestamp": 1559117940240
                },
                {
                    "LogId": "AWsCq85M2hErXcJYbg7w",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:19:00.240  INFO [openapi-service-api,487dcec58abfc6ce,487dcec58abfc6ce,true] 1 --- [http-nio-80-exec-6] c.k.t.o.service.api.aop.HttpAspect       : post入参args=[[{\"id\":4531,\"msgType\":1,\"pushSuccess\":true},{\"id\":4532,\"msgType\":1,\"pushSuccess\":true},{\"id\":4533,\"msgType\":1,\"pushSuccess\":true}]]",
                    "Timestamp": 1559117940240
                },
                {
                    "LogId": "AWsCsGp9uXjszoOztE42",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:24:00.968  INFO [openapi-service-api,fb3be69ce843dc56,fb3be69ce843dc56,true] 1 --- [http-nio-80-exec-3] c.k.t.o.service.api.aop.HttpAspect       : get入参args=0",
                    "Timestamp": 1559118240968
                },
                {
                    "LogId": "AWsCsGp9uXjszoOztE47",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:24:01.049  INFO [openapi-service-api,b1b8a83046972416,b1b8a83046972416,true] 1 --- [http-nio-80-exec-2] c.k.t.o.service.api.aop.HttpAspect       : method=GET",
                    "Timestamp": 1559118241049
                },
                {
                    "LogId": "AWsCsGp9uXjszoOztE4-",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:24:01.049  INFO [openapi-service-api,b1b8a83046972416,b1b8a83046972416,true] 1 --- [http-nio-80-exec-2] c.k.t.o.service.api.aop.HttpAspect       : get入参args=4535",
                    "Timestamp": 1559118241049
                },
                {
                    "LogId": "AWsCsGp9uXjszoOztE5D",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:24:01.750  INFO [openapi-service-api,e744d00003b81587,e744d00003b81587,true] 1 --- [http-nio-80-exec-7] c.k.t.o.service.api.aop.HttpAspect       : method=POST",
                    "Timestamp": 1559118241750
                },
                {
                    "LogId": "AWsCtQbb2hErXcJYcKSd",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:29:03.273  INFO [openapi-service-api,d4613fe92ebe22e6,d4613fe92ebe22e6,true] 1 --- [http-nio-80-exec-1] c.k.t.o.service.api.aop.HttpAspect       : 方法环绕start.....",
                    "Timestamp": 1559118543273
                },
                {
                    "LogId": "AWsCtQbb2hErXcJYcKSe",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:29:03.273  INFO [openapi-service-api,d4613fe92ebe22e6,d4613fe92ebe22e6,true] 1 --- [http-nio-80-exec-1] c.k.t.o.service.api.aop.HttpAspect       : url=http://testprh.yunassess.com/push/getByOffset",
                    "Timestamp": 1559118543273
                },
                {
                    "LogId": "AWsCtQbb2hErXcJYcKSf",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:29:03.273  INFO [openapi-service-api,d4613fe92ebe22e6,d4613fe92ebe22e6,true] 1 --- [http-nio-80-exec-1] c.k.t.o.service.api.aop.HttpAspect       : method=GET",
                    "Timestamp": 1559118543273
                },
                {
                    "LogId": "AWsCtQbb2hErXcJYcKSj",
                    "InstanceId": "openapi-service-api-c594fd9cd-x76rf",
                    "InstanceIp": "172.16.1.34",
                    "Content": "2019-05-29 16:29:03.284  INFO [openapi-service-api,d4613fe92ebe22e6,d4613fe92ebe22e6,true] 1 --- [http-nio-80-exec-1] c.k.t.o.service.api.aop.HttpAspect       : 方法环绕proceed，出参是 :{\"code\":1,\"data\":[]}",
                    "Timestamp": 1559118543284
                }
            ]
        }
    }
}
```

