**Example 1: 获取忽略白名单**

获取忽略白名单

Input: 

```
tccli csip DescribeVulIgnoreRuleList --cli-unfold-argument  \
    --MemberId mem-tencent-6f5795752f66e429 \
    --Limit 10 \
    --Offset 0 \
    --Order desc \
    --By UpdateTime
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppId": 260083796,
                "AssetList": [],
                "AssetRange": 0,
                "Id": 10,
                "Name": "Libvirt iptables规则权限许可和访问控制问题漏洞(CVE-2010-2242)",
                "Remark": "备注1",
                "Switch": 1,
                "UpdateTime": "2026-06-12T07:42:01Z"
            }
        ],
        "Total": 2,
        "RequestId": "f100017b-0d6d-4693-b9e2-9d5baca191fb"
    }
}
```

