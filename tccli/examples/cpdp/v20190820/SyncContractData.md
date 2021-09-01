**Example 1: 签约状态同步接口**



Input: 

```
tccli cpdp SyncContractData --cli-unfold-argument  \
    --MidasAppId SAM001 \
    --SubAppId xxx \
    --UserId taddeng111 \
    --Channel wechat \
    --OutContractCode miketest_contract_0511001 \
    --ContractStatus CONTRACT_STATUS_SIGNED \
    --MidasEnvironment dev \
    --MidasSignature xxx \
    --MidasSecretId xxxx \
    --ContractSyncInfo.ExternalReturnContractInfo.ExternalReturnAgreementId sdsdsds \
    --ContractSyncInfo.ExternalReturnContractInfo.ExternalReturnContractData sdsdsds \
    --ContractSyncInfo.ExternalReturnContractInfo.ExternalReturnContractStatus 1620872255 \
    --ContractSyncInfo.ExternalReturnContractInfo.ExternalReturnRequestId ExternalReturnRequestId \
    --ContractSyncInfo.ExternalContractUserInfo.0.ExternalUserType User_Id \
    --ContractSyncInfo.ExternalContractUserInfo.0.ExternalUserId taddeng111 \
    --ContractSyncInfo.ContractMethod APP-GENERAL \
    --ContractSyncInfo.ExternalReturnContractInfo.ExternalReturnContractEffectiveTimestamp xxxx \
    --ContractSyncInfo.ExternalReturnContractInfo.ExternalReturnContractTerminationTimestamp xxx \
    --ContractSyncInfo.ExternalReturnContractInfo.ExternalReturnContractSignedTimestamp xxxxx \
    --ContractSyncInfo.ExternalReturnContractInfo.ExternalReturnContractExpiredTimestamp xx
```

Output: 
```
{
    "Response": {
        "RequestId": "0b4d0899-6bc5-4261-acc8-29c1f3d29882",
        "Msg": ""
    }
}
```

