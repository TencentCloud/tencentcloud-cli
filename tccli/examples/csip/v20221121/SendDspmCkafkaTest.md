**Example 1: SendCkafkaTest**



Input: 

```
tccli csip SendDspmCkafkaTest --cli-unfold-argument  \
    --VipType 0 \
    --InstanceId ins-2w3ed \
    --Vip 127.0.0.1 \
    --Vport 3306 \
    --Domain www.domain.com \
    --DomainPort 3307 \
    --Username root \
    --Password root@pwd
```

Output: 
```
{
    "Response": {
        "RequestId": "d0f51893-e15f-44ac-be6d-900450a6b8c2"
    }
}
```

