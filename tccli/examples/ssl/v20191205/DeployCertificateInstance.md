**Example 1: 证书部署到clb云资源实例列表**

证书部署到clb云资源实例列表

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
        "DeployStatus": 0,
        "DeployRecordId": 1,
        "RequestId": "xx"
    }
}
```

