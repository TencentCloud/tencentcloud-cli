**Example 1: 修改域名投递状态**



Input: 

```
tccli waf ModifyDomainPostAction --cli-unfold-argument  \
    --Domain www.test.com \
    --PostCLSAction 1 \
    --PostCKafkaAction 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a20702ee-7206-4eeb-ba74-d13ecbc29c02"
    }
}
```

