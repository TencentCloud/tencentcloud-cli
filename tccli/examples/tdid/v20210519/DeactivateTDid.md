**Example 1: 更新DID标识的禁用状态**

更新DID标识的禁用状态

Input: 

```
tccli tdid DeactivateTDid --cli-unfold-argument  \
    --Did did:tdid:w1:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb \
    --OperateCredential {
	"cptId": 1,
	"issuer": "did:tdid:w1:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb",
	"expirationDate": "2023-12-01T10:00:00+08:00",
	"issuanceDate": "2023-09-19T19:50:52+08:00",
	"context": "https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1",
	"id": "250d0563e9d680c4d2c33b428913442f",
	"type": ["VerifiableCredential"],
	"credentialSubject": {
		"action": "deactiveDid",
		"deactivated": "true",
		"did": "did:tdid:w1:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb"
	},
	"proof": {
		"created": "2023-09-19T19:50:52+08:00",
		"creator": "did:tdid:c5:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb#keys-0",
		"signatureValue": "MEYCIQDSQFpHNt7xltx+dPhwHDrY3kJpMG+hE7Klh/c11Ce3WQIhAOFaISj1kvk8TjrlMaoTAAhoAiriBFj0lLwWyNp69kW7",
		"type": "Secp256r1",
		"metaDigest": "9b916ba1e4435f752052fbafe3ed270b61f729feade30fec20aeef4dbac16712",
		"vcDigest": "692c38a285093f538821f7cce3ddc8358f10f219e991faf226356043228eda24",
		"privacy": "Public",
		"salt": {
			"action": "CTtap",
			"deactivated": "1jfRX",
			"did": "D8ukJ"
		}
	}
} \
    --DAPId 5
```

Output: 
```
{
    "Response": {
        "Transaction": {
            "TransactionHash": "17a6bfc02e84d8afca728a0285e5cfc20812a7ca5e0244188a1fdb12cf402789"
        },
        "RequestId": "018647ac-f5ef-478e-bc7c-1e72ae4afac1"
    }
}
```

