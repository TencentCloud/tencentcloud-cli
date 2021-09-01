**Example 1: 添加四层转发规则**



Input: 

```
tccli dayu CreateNewL4Rules --cli-unfold-argument  \
    --Business bgpip \
    --IdList bgpip-0000011t \
    --VipList 129.28.240.44 \
    --Rules.0.RuleName test \
    --Rules.0.Protocol TCP \
    --Rules.0.VirtualPort 18888 \
    --Rules.0.SourcePort 18888 \
    --Rules.0.SourceType 2 \
    --Rules.0.LbType 1 \
    --Rules.0.KeepTime 300 \
    --Rules.0.SourceList.0.Source 1.1.1.10 \
    --Rules.0.SourceList.0.Weight 100 \
    --Rules.0.SourceList.1.Source 1.1.1.20 \
    --Rules.0.SourceList.1.Weight 100 \
    --Rules.0.KeepEnable 0
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

