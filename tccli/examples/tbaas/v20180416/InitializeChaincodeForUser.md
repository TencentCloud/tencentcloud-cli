**Example 1: InitializeChaincodeForUser**



Input: 

```
tccli tbaas InitializeChaincodeForUser --cli-unfold-argument  \
    --Module transaction \
    --Operation chaincode_init_for_user \
    --ClusterId 251005746envnew \
    --GroupName hellorog \
    --ChaincodeName cc050301 \
    --ChaincodeVersion v1.0 \
    --ChannelName ch042103 \
    --PeerName peer0-neworg02.envnew \
    --Args a 100 b 1
```

Output: 
```
{
    "Response": {
        "RequestId": "0b82b65e-7100-49f1-9f29-e934a8833711",
        "TaskId": 1
    }
}
```

