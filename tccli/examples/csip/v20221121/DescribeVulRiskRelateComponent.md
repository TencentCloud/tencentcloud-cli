**Example 1: 获取漏洞关联组件**

获取漏洞关联组件

Input: 

```
tccli csip DescribeVulRiskRelateComponent --cli-unfold-argument  \
    --VulID 38500 \
    --MemberId mem-*******-6f5795752f66e429
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Name": "libtiff",
                "RelateHostCount": 1
            }
        ],
        "RequestId": "0cf2d323-8cc5-4666-86e6-c79a255e9005"
    }
}
```

