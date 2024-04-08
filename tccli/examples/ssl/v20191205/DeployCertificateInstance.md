**Example 1: 证书部署到clb云资源实例列表**

证书部署到clb云资源实例列表， 若部署的监听器开启了SNI，则InstanceIdList传参需要到域名， 若未开启SNI， InstanceIdList只需要到监听器

Input: 

```
tccli ssl DeployCertificateInstance --cli-unfold-argument  \
    --CertificateId vyRlKIeI \
    --InstanceIdList lb-pk278gkq|lbl-2yju432e lb-mmgz14kg|lbl-5q6yn03o|asdasd.ninghhuang.top
```

Output: 
```
{
    "Response": {
        "DeployRecordId": 1,
        "DeployStatus": 0,
        "RequestId": "abc"
    }
}
```

