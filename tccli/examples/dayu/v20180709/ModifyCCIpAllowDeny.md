**Example 1: Adding IP to HTTP CC protection blacklist/whitelist**



Input: 

```
tccli dayu ModifyCCIpAllowDeny --cli-unfold-argument  \
    --Business bgpip\
    --Id bgpip-000000xe\
    --Method add\
    --Type white\
    --IpList 1.1.1.1 1.1.1.2\
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

**Example 2: Adding IP to HTTPS CC protection blacklist/whitelist**



Input: 

```
tccli dayu ModifyCCIpAllowDeny --cli-unfold-argument  \
    --Business bgpip\
    --Id bgpip-000000xe\
    --Method add\
    --Type white\
    --IpList 1.1.1.1 1.1.1.2\
    --Protocol https\
    --Domain test.com\
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

**Example 3: Removing IP from HTTPS CC protection blacklist/whitelist**



Input: 

```
tccli dayu ModifyCCIpAllowDeny --cli-unfold-argument  \
    --Business bgpip\
    --Id bgpip-000000xe\
    --Method delete\
    --Type white\
    --IpList 1.1.1.1 1.1.1.2\
    --Protocol https\
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

