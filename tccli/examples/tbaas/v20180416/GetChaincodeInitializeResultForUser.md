**Example 1: GetChaincodeInitializeResultForUser**



Input: 

```
tccli tbaas GetChaincodeInitializeResultForUser --cli-unfold-argument  \
    --Module chaincode_mng \
    --Operation chaincode_init_result_for_user \
    --ClusterId 251005746envnew \
    --GroupName NewOrg02 \
    --ChannelName ch042103 \
    --ChaincodeName cc042103 \
    --ChaincodeVersion v1.0 \
    --TaskId 11
```

Output: 
```
{
    "Response": {
        "InitResult": 1,
        "InitMessage": "success",
        "RequestId": "551b801e-6dbe-46be-aa46-f8cc3ff1cd09"
    }
}
```

