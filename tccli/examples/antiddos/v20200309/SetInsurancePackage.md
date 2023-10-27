**Example 1: 对ip配置保险包**

新购资产，对ip配置保险包

Input: 

```
tccli antiddos SetInsurancePackage --cli-unfold-argument  \
    --IpList 1.11.1.1 2.2.2.2 \
    --DevType lighthouse \
    --InstanceId lhins-xxxxxxx \
    --Operation create
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

