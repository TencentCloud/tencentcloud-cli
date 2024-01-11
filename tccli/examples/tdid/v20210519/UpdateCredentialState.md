**Example 1: 更新凭证链上状态**

更新凭证链上状态

Input: 

```
tccli tdid UpdateCredentialState --cli-unfold-argument  \
    --DAPId 5 \
    --OperateCredential {
	"cptId": 1,
	"issuer": "did:tdid:w1:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb",
	"expirationDate": "2023-12-01T10:00:00+08:00",
	"issuanceDate": "2023-09-19T20:13:36+08:00",
	"context": "https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1",
	"id": "fw1652844bee8e5ecf1b404242b83f1b",
	"type": ["VerifiableCredential"],
	"credentialSubject": {
		"CredentialStatus": {
			"id": "8818fdd61eb84e4a745a3b04c96e5237",
			"issuer": "did:tdid:w1:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb",
			"status": 1
		},
		"action": "updateCredentialState",
		"orignCredential": "{\"cptId\":1,\"issuer\":\"did:tdid:w1:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb\",\"expirationDate\":\"2023-12-01T10:00:00+08:00\",\"issuanceDate\":\"2023-09-19T20:04:20+08:00\",\"context\":\"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1\",\"id\":\"8818fdd61eb84e4a745a3b04c96e5237\",\"type\":[\"VerifiableCredential\"],\"credentialSubject\":{\"action\":\"updateCredentialState\"},\"proof\":{\"created\":\"2023-09-19T20:04:20+08:00\",\"creator\":\"did:tdid:w1:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb#keys-0\",\"signatureValue\":\"MEUCIQDUneIwlLbh5AFjQt9HJhIZAQshT45/Em8hVOUjHcdu0QIgL3rg3A99qGGNszstF+GTV5IU4vT9OnI1lqM3f0w1JmI=\",\"type\":\"Secp256r1\",\"metaDigest\":\"6a216f84cb9w1b6170cb017cccd6w1d0b81aad200d5691914d6045471d0dd1ad\",\"vcDigest\":\"c7e13w1bcfa879c922f9141d085facc0ce1973e8d27d48238130739c1a332dcf\",\"privacy\":\"Public\",\"salt\":{\"action\":\"HZdDU\"}}}"
	},
	"proof": {
		"created": "2023-09-19T20:13:36+08:00",
		"creator": "did:tdid:w1:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb#keys-0",
		"signatureValue": "MEUCIDkLg6EqmwvEHYLtjumpeqKz/hIi6EROMDXPPpNIxORHAiEA8T0LMI59tkBTz+llu/GkjToj5M8k5SwXFoU3fnjQ3mo=",
		"type": "Secp256r1",
		"metaDigest": "46894b7f54365d685ba587608d2b74f800404ebb76f5c32dd90bc3916e844ae2",
		"vcDigest": "d086ba831ab3185971c168w125bf2bd487d7eced3ede8d623b30cfe9da03bcaf",
		"privacy": "Public",
		"salt": {
			"CredentialStatus": {
				"id": "4dPOH",
				"issuer": "OJH5M",
				"status": "lm2W4"
			},
			"action": "r95wA",
			"orignCredential": "b3H4j"
		}
	}
}
```

Output: 
```
{
    "Response": {
        "RequestId": "f5e12d37-100a-4b82-b522-7b76c519ed70",
        "Result": true
    }
}
```

