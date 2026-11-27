**Example 1: 查询资源绑定的防护实例**

查询负载均衡资源 `lb-6******q` 当前绑定的 DDoS 高防服务防护实例。

Input: 

```
tccli antiddos DescribeResourceProtections --cli-unfold-argument  \
    --Resources qcs::clb:ap-guangzhou:uin/700******996:clb/lb-6******q
```

Output: 
```
{
    "Response": {
        "ResourceProtections": [
            {
                "Resource": "qcs::clb:ap-guangzhou:uin/700*******96:clb/lb-6******q",
                "ProtectionId": "prot-3sk*******py"
            }
        ],
        "RequestId": "3a0775ce-60d6-4c3b-9c91-021fbe50dd5a"
    }
}
```

