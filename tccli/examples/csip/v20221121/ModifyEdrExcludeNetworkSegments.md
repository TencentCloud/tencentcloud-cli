**Example 1: 修改EDR日志采集例外网段配置**

修改EDR日志采集例外网段配置

Input: 

```
tccli csip ModifyEdrExcludeNetworkSegments --cli-unfold-argument  \
    --NetworkSegments 100.64.0.0/10 192.168.0.0/24
```

Output: 
```
{
    "Response": {
        "RequestId": "1c26308c-5493-4eaf-a817-112ec25f499e"
    }
}
```

