**Example 1: GetAuthoritiesList**

权威机构列表

Input: 

```
tccli tdid GetAuthoritiesList --cli-unfold-argument  \
    --Did did:tdid:15:0xf1cefdd7991234c7a52d69225012ba0eaef7025d \
    --Status 1 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "ResultList": [
            {
                "Id": 39,
                "DidId": 5721,
                "Did": "did:tdid:15:0xf1cefdd7991234c7a52d69225012ba0eaef7025d",
                "Name": "tencent",
                "Status": 1,
                "DidServiceId": 25,
                "ContractAppId": 45,
                "Remark": "tx",
                "RegisterTime": "2021-08-03 09:58:54",
                "RecognizeTime": "2021-08-03 15:36:06",
                "CreateTime": "2021-08-03 09:58:54",
                "UpdateTime": "2021-08-03 09:58:54",
                "ClusterId": "bcos-fmtkyt8xne",
                "GroupId": 15,
                "AppName": "xxxxx",
                "LabelName": ""
            }
        ],
        "AllCount": 1,
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

