**Example 1: Adding URL to HTTP CC protection blacklist/whitelist**



Input: 

```
tccli dayu ModifyCCUrlAllow --cli-unfold-argument  \
    --Business bgpip\
    --Id bgpip-000000xe\
    --Method add\
    --Type white\
    --UrlList http://www.123.com/index.html www.456.com/buy.html\
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

**Example 2: Adding URL to HTTPS CC protection blacklist/whitelist**



Input: 

```
tccli dayu ModifyCCUrlAllow --cli-unfold-argument  \
    --Business bgpip\
    --Id bgpip-000000xe\
    --Method add\
    --Type white\
    --UrlList http://www.123.com/index.html www.456.com/buy.html\
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

**Example 3: Removing URL from HTTPS CC protection blacklist/whitelist**



Input: 

```
tccli dayu ModifyCCUrlAllow --cli-unfold-argument  \
    --Business bgpip\
    --Id bgpip-000000xe\
    --Method delete\
    --Type white\
    --UrlList http://www.123.com/index.html www.456.com/buy.html\
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

