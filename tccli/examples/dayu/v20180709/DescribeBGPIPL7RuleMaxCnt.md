**Example 1: 获取高防IP可添加的最多7层规则数量**



Input: 

```
tccli dayu DescribeBGPIPL7RuleMaxCnt --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-0000000e
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Count": 1
    }
}
```

