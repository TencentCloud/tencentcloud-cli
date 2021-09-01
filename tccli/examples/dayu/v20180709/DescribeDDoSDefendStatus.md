**Example 1: 获取DDoS防护状态**



Input: 

```
tccli dayu DescribeDDoSDefendStatus --cli-unfold-argument  \
    --Business base \
    --Ip 1.1.1.1 \
    --BizType public \
    --.DeviceType cvm \
    --InstanceId ins-f2f9ssbo \
    --IPRegion gz
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "DefendStatus": 0,
        "UndefendExpire": "2019-11-14 15:00:00",
        "ShowFlag": 1
    }
}
```

