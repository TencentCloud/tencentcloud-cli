**Example 1: 创建策略**



Input: 

```
tccli csip ModifyEDRRule --cli-unfold-argument  \
    --RuleType 1 \
    --AlertAction 1 \
    --CWPScope 1 \
    --TCSSScope 1 \
    --Status 1 \
    --MemberId mem-tencent-e74488e0ba0cd8fe \
    --Name 白名单3 \
    --ContentType ip_outbound \
    --Level 1 \
    --DetectMode 1 \
    --AttackStage TA0043 \
    --RuleID 44ff42d6-70ee-4d20-84ad-5240d8286a07 \
    --Description 白名单 \
    --DealOldEvents 0 \
    --Md5List 098f6bcd4621d373cade4e832627b4f6 \
    --FileName L3Vzci9sb2MvYmlu \
    --FileDirectory L3Vzci9sb2MvYmlu \
    --CmdLineRules.Process.Exe /usr/local/bin \
    --CmdLineRules.Process.CmdLine /test3 \
    --CmdLineRules.ParentProcess.Exe /usr/local/bin \
    --CmdLineRules.ParentProcess.CmdLine /test3 \
    --CmdLineRules.AncestorProcess.Exe /usr/local/bin \
    --CmdLineRules.AncestorProcess.CmdLine /test3 \
    --Domains d3d3LmJhaWR1LmNvbQ== \
    --OutboundIP MS4xLjEuNw== \
    --InboundIP MS4xLjEuNw== \
    --ImageIDs 'sha256: 3599d4bcee082427c6b335a5b0d98892d2f5f0d7b1e5dc49c12e882f0f4a133f' \
    --ProcessNetworkRules.Process.Exe /usr/local/bin \
    --ProcessNetworkRules.Process.CmdLine /test3 \
    --ProcessNetworkRules.DstIP 1.1.1.1-1.1.1.10 \
    --ProcessNetworkRules.ParentProcess.Exe /usr/local/bin \
    --ProcessNetworkRules.ParentProcess.CmdLine /test3 \
    --ProcessNetworkRules.DstPorts 222 \
    --TargetAppIDs 260199983
```

Output: 
```
{
    "Response": {
        "RequestId": "8fdad8e2-2e71-4da5-bf68-836743e6231a"
    }
}
```

