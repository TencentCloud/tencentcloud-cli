**Example 1: 证书部署到clb云资源实例列表**

证书部署到clb云资源实例列表， 若部署的监听器开启了SNI，则InstanceIdList传参需要到域名， 若未开启SNI， InstanceIdList只需要到监听器； 
公共参数Region必传， Region表示操作clb对应地域的资源

Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList lb-pk278gkq|lbl-2yju432e lb-mmgz14kg|lbl-5q6yn03o|clb1.tencent.com \
    --ResourceType clb
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 2: 证书部署到cdn云资源域名列表**



Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList cdn1.tencent.com|off cdn2.tencent.com|on \
    --ResourceType cdn
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 3: 证书部署到edgeOne云资源域名列表**



Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList edgeone1.tencent.com edgeone2.tencent.com \
    --ResourceType teo
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 4: 证书部署到ddos云资源实例列表**



Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList bgpip-000001ms|tencent.com|443 \
    --ResourceType ddos
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 5: 证书部署到waf域名列表**



Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList waf1.tencent.com waf2.tencent.com \
    --ResourceType waf
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 6: 证书部署到云直播域名列表**



Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList live1.tencent.com live2.tencent.com \
    --ResourceType live
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 7: 证书部署到apigateway云资源域名列表**

公共参数Region必传， Region表示操作api网关对应地域的资源

Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList service-8sk7cqmd|apigw1.tencent.com service-8sk7cqmd|apigw2.tencent.com \
    --ResourceType apigateway
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 8: 证书部署到tke云资源实例列表**

公共参数Region必传， Region表示操作tke对应地域的资源

Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList cls-42sa0ae0|default|test-tencent \
    --ResourceType tke
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 9: 证书部署到cos云资源实例列表**

公共参数Region必传， Region表示操作cos对应地域的资源

Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList ap-hongkong#ssl-server-1251810746#tencent.com \
    --ResourceType cos
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 10: 证书部署到lighthouse云资源实例列表**

公共参数Region必传， Region表示操作lighthouse对应地域的资源

Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList ap-shanghai|lhins-nh7lql34|tencent.com \
    --ResourceType lighthouse
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 11: 证书部署到tse云资源实例列表**

公共参数Region必传， Region表示操作tse对应地域的资源

Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList gateway-s1da9151|fa61bc05-cc54-4eea-c932-24de52577372 \
    --ResourceType tse
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 12: 证书部署到tcb云资源实例列表**

公共参数Region必传， Region表示操作tcb对应地域的资源

Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList AccessService|ap-shanghai|ceshi-4s5h0ymg11c839c7|tencent.com \
    --ResourceType tcb
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

**Example 13: 证书部署到云点播域名列表**



Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList vod1.tencent.com vod2.tencent.com \
    --ResourceType vod
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

