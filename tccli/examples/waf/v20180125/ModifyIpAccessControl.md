**Example 1: 编辑IP黑白名单**



Input: 

```
tccli waf ModifyIpAccessControl --cli-unfold-argument  \
    --InstanceId waf_accc \
    --Domain www.qcloudwaf.com \
    --IpList 192.168.1.1 192.168.1.2 \
    --Edition clb-waf \
    --SourceType batch \
    --RuleId 5512222 \
    --ActionType 42 \
    --ValidTS 0 \
    --Note abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

