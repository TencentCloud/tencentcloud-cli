**Example 1: 调用示例**



Input: 

```
tccli ai3d DescribeAutoRiggingJob --cli-unfold-argument  \
    --JobId 1445334238810423296
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "ResultFile3Ds": [
            {
                "Type": "FBX",
                "Url": "https://*******************.cos.ap-guangzhou.tencentcos.cn/auto_rigging/output/251197750/0505fe2f-db7d-4ff3-9042-fee009749664_0.fbx?q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1778488950%3B1778575349&q-key-time=1778488950%3B1778575349&q-header-list=host&q-url-param-list=&q-signature=8d15859d57e2da3acd6bac9fba12b724baf549ba"
            }
        ],
        "Status": "DONE",
        "RequestId": "06201b08-dbe4-4fa6-8a16-c7f574c33824"
    }
}
```

