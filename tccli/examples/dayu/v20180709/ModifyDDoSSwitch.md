**Example 1: 开启或关闭DDoS防护**



Input: 

```
tccli dayu ModifyDDoSSwitch --cli-unfold-argument  \
    --Business basic \
    --Method set \
    --Status 0 \
    --Ip 1.1.1.1 \
    --BizType public \
    --DeviceType cvm \
    --InstanceId cvm-abdcasddd1 \
    --IPRegion gz
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Status": 0
    }
}
```

