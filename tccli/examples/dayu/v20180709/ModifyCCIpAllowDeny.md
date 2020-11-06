**Example 1: 添加HTTP协议的CC防护IP黑白名单**



Input: 

```
tccli dayu ModifyCCIpAllowDeny --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Method add \
    --Type white \
    --IpList 1.1.1.1 1.1.1.2 \
    --Protocol http
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

**Example 2: 添加HTTPS协议的CC防护IP黑白名单**



Input: 

```
tccli dayu ModifyCCIpAllowDeny --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Method add \
    --Type white \
    --IpList 1.1.1.1 1.1.1.2 \
    --Protocol https \
    --Domain test.com \
    --RuleId rule-0000001
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

**Example 3: 删除HTTPS协议的CC防护IP黑白名单**



Input: 

```
tccli dayu ModifyCCIpAllowDeny --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Method delete \
    --Type white \
    --IpList 1.1.1.1 1.1.1.2 \
    --Protocol https \
    --Domain test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

