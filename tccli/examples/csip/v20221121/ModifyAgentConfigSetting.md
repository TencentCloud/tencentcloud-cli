**Example 1: 设置**



Input: 

```
tccli csip ModifyAgentConfigSetting --cli-unfold-argument  \
    --MemberId mem-tencent-b624e485fee5fe29 \
    --LogCollectSettings tcp_ingress \
    --AssetSelectionType direct \
    --TagIds 1 \
    --InstanceIDs ins-q4pf14qs \
    --ExcludeInstanceIDs ins-q4pf14qs
```

Output: 
```
{
    "Response": {
        "RequestId": "be9df78e-7319-4584-a283-c34381b1fd31"
    }
}
```

