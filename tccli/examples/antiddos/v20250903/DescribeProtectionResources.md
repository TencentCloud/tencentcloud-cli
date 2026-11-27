**Example 1: 查询防护实例的防护资源列表**

查询防护实例 `prot-3x7powyzy7kx` 下绑定的防护资源，返回第 1 页、每页 20 条。

Input: 

```
tccli antiddos DescribeProtectionResources --cli-unfold-argument  \
    --ProtectionId prot-3x7powyzy7kx \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ResourceInfos": [
            {
                "Resource": "qcs::clb:ap-guangzhou:uin/7000****8005:clb/lb-jm****74",
                "ResourceType": "clb",
                "Status": "protecting",
                "Region": "ap-guangzhou",
                "PublicAddresses": [
                    "lb-jmn***74-u8ovwq****xdj02f.clb.gz-ten****clb.com"
                ]
            }
        ],
        "RequestId": "2a146867-7e3f-4854-8e0d-f37cb1c6dd51"
    }
}
```

