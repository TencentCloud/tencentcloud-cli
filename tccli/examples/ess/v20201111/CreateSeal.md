**Example 1: 创建企业电子印章**



Input: 

```
tccli ess CreateSeal --cli-unfold-argument  \
    --Operator.UserId yDt2RUUckpfnij59UEF24JRO0rtOBcfq \
    --SealName ceshi \
    --SealSize 42_42 \
    --SealType OTHER
```

Output: 
```
{
    "Response": {
        "ImageUrl": "https://file.ess.tencent.cn/bresource/resource/resource/0/0.PNG?hkey=fa8b8ce5d7dcf25fc59ffb546fd5cbaf7ed002d7828ebfce597c2d5ce5ed99512d44b2e3e10f26498787639a93e7505f74d20125094e0a881938826d043be378b0aba5b586d651b4e08f8ea244c4053b&sign=713cc886c0292549929cb6d65757b21ad59079bbe535bc04a68f78df61dc2670",
        "PreviewFileUrl": "",
        "PreviewPdfUrl": "",
        "RequestId": "62e859ea-9218-436a-bdce-3d94d6c56fe0",
        "SealId": "yD3JaUUckpelefu5UxsWLnwv3JrS25PH",
        "SealOperatorVerifyPath": "",
        "SealOperatorVerifyQrcodeUrl": ""
    }
}
```

