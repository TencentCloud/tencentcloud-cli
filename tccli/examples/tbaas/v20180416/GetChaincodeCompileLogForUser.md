**Example 1: GetChaincodeCompileLogForUser**



Input: 

```
tccli tbaas GetChaincodeCompileLogForUser --cli-unfold-argument  \
    --Module chaincode_mng \
    --Operation chaincode_compile_log_for_user \
    --ClusterId 251005746envnew \
    --GroupName hellorog \
    --ChaincodeName cc050301 \
    --ChaincodeVersion v1.0 \
    --PeerName peer0-neworg02.envnew \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "CompileLogList": [
            {
                "LineNumber": 0,
                "LogMessage": "peer0-NewOrg02.envnew"
            }
        ],
        "RequestId": "3f6836c5-e889-431e-b932-47a1653c5f7b"
    }
}
```

