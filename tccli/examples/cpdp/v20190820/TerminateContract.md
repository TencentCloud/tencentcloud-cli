**Example 1: 解除签约关系接口**



Input: 

```
tccli cpdp TerminateContract --cli-unfold-argument  \
    --MidasAppId SAM001 \
    --SubAppId xxx \
    --UserId taddeng111 \
    --Channel wechat \
    --TerminateMode CONTRACT_TERMINATION_MODE_BY_OUT_CONTRACT_CODE \
    --OutContractCode miketest_contract_0512001 \
    --ContractSceneId APP-GENERAL \
    --ChannelContractCode xxx \
    --ExternalContractData xxx \
    --TerminationReason testreason测试原因 \
    --MidasSecretId xxx \
    --MidasSignature xxxx \
    --MidasEnvironment dev
```

Output: 
```
{
    "Response": {
        "ContractTerminateData": {
            "ExternalReturnMessage": "",
            "ExternalReturnCode": "SUCCESS",
            "ExternalReturnData": ""
        },
        "Msg": "",
        "RequestId": "cb99c2eb-4581-42bc-9f7b-a18571264f91"
    }
}
```

