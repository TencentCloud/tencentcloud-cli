**Example 1: 新增IP黑白名单**



Input: 

```
tccli waf CreateIpAccessControl --cli-unfold-argument  \
    --InstanceId waf_0xabc \
    --Domain www.qcloudwaf.com \
    --IpList 192.168.1.1 192.168.2.1 \
    --Edition clb-waf \
    --ValidTS 1680570420 \
    --ActionType 42 \
    --SourceType custom
```

Output: 
```
{
    "Response": {
        "RuleId": 55201922,
        "RequestId": "fea2e723-002b-40e6-8297-7c54455cb7d6"
    }
}
```

