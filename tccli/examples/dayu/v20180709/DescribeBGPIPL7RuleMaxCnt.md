**Example 1: Getting the maximum number of layer-7 rules that can be added to an Anti-DDoS Advanced instance**



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

