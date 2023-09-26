**Example 1: 创建 CNAME 接入类型的站点**

创建 CNAME 接入类型的站点 example.com，服务区域为全球可用区，绑定套餐 edgeone-37q0w6qali10。接口将返回站点 ID 和站点归属权验证信息。您可以对站点进行归属权验证，可参考 [站点/域名归属权验证](https://cloud.tencent.com/document/product/1552/70789)。

Input: 

```
tccli teo CreateZone --cli-unfold-argument  \
    --Type partial \
    --ZoneName example.com \
    --Area global \
    --PlanId edgeone-37q0w6qali10
```

Output: 
```
{
    "Response": {
        "ZoneId": "zone-27q0p0bali16",
        "OwnershipVerification": {
            "DnsVerification": {
                "Subdomain": "edgeonereclaim",
                "RecordType": "TXT",
                "RecordValue": "reclaim-a24aba2420cf4ce8b7bff7c8be6d337f"
            },
            "FileVerification": {
                "Path": "/.well-known/teo-verification/vd4ewuqa9n.txt",
                "Content": "88v24mnnljwbhaohrpfx80f63duhdnjx"
            },
            "NsVerification": null
        },
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

**Example 2: 创建 NS 接入类型的站点 **

创建NS接入模式站点 example.com，服务区域为中国大陆可用区，绑定套餐 edgeone-37q0w6qali10。接口将返回 DNS 服务器信息，您需要前往域名注册商处修改，可参考 [修改 DNS 服务器](https://cloud.tencent.com/document/product/1552/90452)。

Input: 

```
tccli teo CreateZone --cli-unfold-argument  \
    --Type full \
    --ZoneName example.com \
    --Area mainland \
    --PlanId edgeone-37q0w6qali10
```

Output: 
```
{
    "Response": {
        "ZoneId": "zone-27q0p0bali16",
        "OwnershipVerification": {
            "DnsVerification": null,
            "FileVerification": null,
            "NsVerification": {
                "NameServers": [
                    "ns1.teodns.com",
                    "ns2.teodns.com"
                ]
            }
        },
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

**Example 3: 创建无域名接入模式站点**

创建无域名接入模式站点，绑定套餐 edgeone-37q0w6qali10。接口将返回站点 ID。有关无域名接入模式的相关信息，可参考 [快速启用四层代理服务](https://cloud.tencent.com/document/product/1552/96051)。

Input: 

```
tccli teo CreateZone --cli-unfold-argument  \
    --Type noDomainAccess \
    --PlanId edgeone-37q0w6qali10
```

Output: 
```
{
    "Response": {
        "ZoneId": "zone-27q0p0bali16",
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

