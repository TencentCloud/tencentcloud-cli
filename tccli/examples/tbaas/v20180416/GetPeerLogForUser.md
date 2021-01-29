**Example 1: GetPeerLogForUser**



Input: 

```
tccli tbaas GetPeerLogForUser --cli-unfold-argument  \
    --Module peer_mng \
    --Operation peer_log_for_user \
    --ClusterId 251005746envnew \
    --GroupName hellorog \
    --PeerName peer0-neworg02.envnew \
    --BeginTime 2020-11-24 19:49:25 \
    --RowNum 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PeerLogList": [
            {
                "LogMessage": "peer0-NewOrg02.envnew",
                "LineNumber": 1
            }
        ],
        "RequestId": "3f6836c5-e889-431e-b932-47a1653c5f7b"
    }
}
```

