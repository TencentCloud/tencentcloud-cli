**Example 1: 管理云梯内网CLB**

管理云梯内网CLB

Input: 

```
tccli tse ManageCLB --cli-unfold-argument  \
    --SubnetId subnet-xxxxx \
    --InstanceId ins-xxxx \
    --VpcId vpc-123456 \
    --Command create \
    --EngineRegion ap-beijing \
    --Vip 10.0.0.1
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "3a2e00dd-1870-44b8-8b45-73ca8064ec47"
    }
}
```

