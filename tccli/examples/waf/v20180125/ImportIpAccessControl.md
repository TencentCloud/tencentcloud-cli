**Example 1: 导入IP黑白名单**



Input: 

```
tccli waf ImportIpAccessControl --cli-unfold-argument  \
    --Domain www.qcloudwaf.com \
    --Data.0.IpList 2.3.4.5 \
    --Data.0.ValidTs 1709222399 \
    --Data.0.ActionType 42 \
    --Data.0.Note  \
    --Data.1.IpList 2.3.4.6 \
    --Data.1.ValidTs 1709222399 \
    --Data.1.ActionType 42 \
    --Data.1.Note  \
    --InstanceId waf_2kxt4nou00atrvn1 \
    --SourceType custom
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

