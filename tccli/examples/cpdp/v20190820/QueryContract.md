**Example 1: 查询签约关系**



Input: 

```
tccli cpdp QueryContract --cli-unfold-argument  \
    --MidasAppId SAM001 \
    --SubAppId xxx \
    --UserId taddeng111 \
    --Channel wechat \
    --ContractQueryMode CONTRACT_QUERY_MODE_BY_OUT_CONTRACT_CODE \
    --OutContractCode miketest_contract_0511001 \
    --ContractSceneId APP-GENERAL \
    --ChannelContractCode xxx \
    --ExternalContractData xxx \
    --MidasEnvironment dev \
    --MidasSignature xxx \
    --MidasSecretId xxxx
```

Output: 
```
{
    "Response": {
        "Msg": "",
        "RequestId": "b9469088-bd71-4ccf-99fe-6fd51e6a29c6",
        "ContractData": {
            "ChannelSubMerchantId": "",
            "ChannelAppId": "SAM001",
            "ChannelName": "wechat",
            "ExternalReturnCode": "SUCCESS",
            "ExternalReturnMessage": "",
            "ExternalReturnData": "<xml><return_code><![CDATA[SUCCESS]]></return_code>\n<result_code><![CDATA[SUCCESS]]></result_code>\n<mch_id><![CDATA[1600317581]]></mch_id>\n<appid><![CDATA[wxa384c55535723da0]]></appid>\n<contract_id><![CDATA[202105115706341423]]></contract_id>\n<plan_id>138096</plan_id>\n<openid><![CDATA[o6khq5FNTcJTADCsk9uXSV6djzvE]]></openid>\n<request_serial>1620703959</request_serial>\n<contract_code><![CDATA[miketest_contract_0511001]]></contract_code>\n<contract_display_account><![CDATA[甘丽娜]]></contract_display_account>\n<contract_state>1</contract_state>\n<contract_signed_time><![CDATA[2021-05-11 11:34:22]]></contract_signed_time>\n<contract_expired_time><![CDATA[2031-05-09 11:34:22]]></contract_expired_time>\n<contract_terminated_time><![CDATA[2021-05-11 20:41:07]]></contract_terminated_time>\n<contract_termination_mode>3</contract_termination_mode>\n<contract_termination_remark><![CDATA[test]]></contract_termination_remark>\n<err_code>0</err_code>\n<err_code_des><![CDATA[SUCCESS]]></err_code_des>\n<sign><![CDATA[AF82AA6BA9B3064F54FEC7C3B104ABAC]]></sign>\n</xml>",
            "NotifyUrl": "https://dev.tke.midas.qq.com/node/vereinen/util/dump/empty_req/post",
            "ChannelSubAppId": "",
            "ChannelMerchantId": "SAM001",
            "ReturnContractInfo": {
                "ChannelReturnContractInfo": {
                    "ContractStatus": "CONTRACT_STATUS_TERMINATED",
                    "ChannelContractInfo": {
                        "ChannelContractCode": "miketest_contract_0511001",
                        "OutContractCode": "miketest_contract_0511001"
                    }
                },
                "ExternalReturnContractInfo": {
                    "ExternalReturnContractSignedTimestamp": "2021-05-11T11:34:22Z",
                    "ExternalReturnContractTerminationTimestamp": "2021-05-11T20:41:07Z",
                    "ExternalReturnContractEffectiveTimestamp": "1970-01-01T00:00:00Z",
                    "ExternalReturnAgreementId": "202105115706341423",
                    "ExternalReturnContractData": "{\"contract_id\":\"202105115706341423\"}",
                    "ExternalReturnRequestId": "1620703959",
                    "ExternalReturnContractTerminationRemark": "test",
                    "ExternalReturnContractExpiredTimestamp": "2031-05-09T11:34:22Z",
                    "ExternalReturnContractStatus": "CONTRACT_STATUS_TERMINATED",
                    "ExternalReturnContractTerminationMode": "CONTRACT_TERMINATION_MODE_TERMINATED_BY_MERCHANT_API"
                },
                "ContractInfo": {
                    "ChannelContractMerchantId": "SAM001",
                    "ChannelContractSubMerchantId": "",
                    "ChannelContractSubAppId": "",
                    "ContractSceneId": "APP-GENERAL",
                    "ContractMethod": "wechat_jsapi",
                    "ChannelContractAppId": "SAM001",
                    "ExternalContractUserInfoList": [],
                    "UserInfo": {
                        "UserType": "USER_ID",
                        "UserId": "taddeng111"
                    },
                    "OutContractCode": "miketest_contract_0511001",
                    "ExternalContractData": ""
                }
            }
        }
    }
}
```

