**Example 1: 漏洞修护-查询可修护主机信息**

漏洞修护-查询可修护主机信息

Input: 

```
tccli cwp DescribeCanFixVulMachine --cli-unfold-argument  \
    --VulIds 1 \
    --Quuids a0770b41-9697-4a1d-8150-b8fa********
```

Output: 
```
{
    "Response": {
        "RequestId": "48ca3c70-801e-48b1-80a7-1007afbf5ffb",
        "VulInfo": []
    }
}
```

