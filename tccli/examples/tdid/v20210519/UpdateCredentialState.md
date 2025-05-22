**Example 1: 无需凭证鉴权首次更新凭证链上状态**

用于颁发凭证的DID标识是本腾讯云账号创建的场景
由于凭证颁发凭证的DID是本账号创建默认拥有设置凭证状态权限，因此不需操作鉴权的临时凭证
OperateCredential不需设置，CredentialStatus为凭证状态信息，OriginCredential携带原始凭证的内容

Input: 

```
tccli tdid UpdateCredentialState --cli-unfold-argument  \
    --DAPId 51 \
    --CredentialStatus.Id 617481bf42ad384b3324551cb2f454be \
    --CredentialStatus.Issuer did:tdid:c2:0x379106c7232aed1a50e8600511655b479c76b149 \
    --CredentialStatus.Status 1 \
    --OriginCredential {"cptId":1,"issuer":"did:tdid:c2:0x379106c7232aed1a50e8600511655b479c76b149","expirationDate":"2124-06-29T15:25:00+08:00","issuanceDate":"2023-11-08T10:06:05+08:00","context":"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1","id":"617481bf42ad384b3324551cb2f454be","type":["VerifiableCredential"],"credentialSubject":{"action":"deactiveDid","age":17},"proof":{"created":"2023-11-08T10:06:05+08:00","creator":"did:tdid:c2:0x379106c7232aed1a50e8600511655b479c76b149#keys-0","signatureValue":"MEUCIQDUHK3znfKQA4XqiyRMgM0C6m/TbaAhzbA5PG3Mi8kFOwIgVnZWkCNrLiPC62ZUDzHfwd5aqh2nQPHpc7hLlRIflyg=","type":"Secp256r1","metaDigest":"3aba1bf7555b79e5217a87e39b5122e3e62d5c486878e6a24f629aed207561cb","vcDigest":"9e71e2b5587517769b126a2877f8b6071cf3aa2389bd57618ba97f07a763984c","privacy":"Public","salt":{"action":"hFify","age":"bEQqg"}}}
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

**Example 2: 需要凭证鉴权首次更新凭证链上状态**

用于颁发凭证的DID标识是非本腾讯云账号创建的场景
由于凭证颁发凭证的DID为非本账号创建，默认无设置凭证状态的权限，因此需要临时凭证进行操作鉴权
OriginCredential和CredentialStatus不需设置，OperateCredential携带建操作鉴权临时凭证,凭证通过IssueCredential接口颁发，凭证参数说明如下：
1. 凭证模板 id (cpt)固定为 1
2. claim需三个字段：
(1) action: 固定为updateCredentialState 
(2) originCredential: 携带待更新状态的凭证原始内容
(3) credentialStatus: 凭证状态结构的json字符串，包括3个字段：
Id: 凭证 id，对应凭证的 id 字段 
issuer:  凭证颁发者 Did  
Status: 凭证状态（0：吊销；1：有效） 
3. ExpirationDate过期时间根据操作凭证创建时间和调用更新凭证状态接口的时间差来设置，通常状态实时更新，过期时间在1分钟内即可

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
		"originCredential": "{\"cptId\":1,\"issuer\":\"did:tdid:w1:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb\",\"expirationDate\":\"2023-12-01T10:00:00+08:00\",\"issuanceDate\":\"2023-09-19T20:04:20+08:00\",\"context\":\"https://github.com/TencentCloud-Blockchain/TDID/blob/main/context/v1\",\"id\":\"8818fdd61eb84e4a745a3b04c96e5237\",\"type\":[\"VerifiableCredential\"],\"credentialSubject\":{\"action\":\"updateCredentialState\"},\"proof\":{\"created\":\"2023-09-19T20:04:20+08:00\",\"creator\":\"did:tdid:w1:0xe0fd109747937fbaf68ef1f615c2cd8e87d22ffb#keys-0\",\"signatureValue\":\"MEUCIQDUneIwlLbh5AFjQt9HJhIZAQshT45/Em8hVOUjHcdu0QIgL3rg3A99qGGNszstF+GTV5IU4vT9OnI1lqM3f0w1JmI=\",\"type\":\"Secp256r1\",\"metaDigest\":\"6a216f84cb9w1b6170cb017cccd6w1d0b81aad200d5691914d6045471d0dd1ad\",\"vcDigest\":\"c7e13w1bcfa879c922f9141d085facc0ce1973e8d27d48238130739c1a332dcf\",\"privacy\":\"Public\",\"salt\":{\"action\":\"HZdDU\"}}}"
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

**Example 3: 凭证状态已上链再次更新状态的场景(非首次更新凭证状态)**

首次更新过凭证状态后，凭证状态已绑定该账号的链上用户，所以后续更新凭证状态只需参数CredentialStatus即可, OperateCredential和OriginCredential参数均不需要

Input: 

```
tccli tdid UpdateCredentialState --cli-unfold-argument  \
    --DAPId 51 \
    --CredentialStatus.Id 617481bf42ad384b3324551cb2f454be \
    --CredentialStatus.Issuer did:tdid:c2:0x379106c7232aed1a50e8600511655b479c76b149 \
    --CredentialStatus.Status 0
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

