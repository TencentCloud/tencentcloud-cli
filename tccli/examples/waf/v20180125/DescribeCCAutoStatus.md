**Example 1: Waf 斯巴达版本查询cc自动封堵状态**



Input: 

```
tccli waf DescribeCCAutoStatus --cli-unfold-argument  \
    --Domain www.test.com
```

Output: 
```
{
    "Response": {
        "AutoCCSwitch": 0,
        "RequestId": "2a2d479f-d481-40e9-bb31-8f9e743bd529"
    }
}
```

