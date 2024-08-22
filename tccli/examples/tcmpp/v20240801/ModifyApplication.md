**Example 1: ModifyApplication**



Input: 

```
tccli tcmpp ModifyApplication --cli-unfold-argument  \
    --ApplicationId app-fa9k2i3c42 \
    --ApplicationName autotest_app0819210523 \
    --Logo https://127.0.0.1T04257DS9431720WTAG/console/20240819210517-6638b98fe1.png \
    --AndroidAppKey com.tencent.tcmpp.demo \
    --IosAppKey com.tencent.tcmpp.demo \
    --Intro 介绍信息 \
    --Remark 描述信息 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "e134087b-0e6c-4e0f-bbfe-e1b481482ff3"
    }
}
```

