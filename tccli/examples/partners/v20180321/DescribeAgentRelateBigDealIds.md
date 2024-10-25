**Example 1: 查询到关联订单示例**

有两笔关联订单的返回。若没有关联订单则返回空数组

Input: 

```
tccli partners DescribeAgentRelateBigDealIds --cli-unfold-argument  \
    --BigDealId 20241021203002223764041
```

Output: 
```
{
    "Response": {
        "BigDealIdList": [
            "20241021203002223736651",
            "20241021203002223761601"
        ],
        "RequestId": "00c9d9d3-432f-44bb-8d76-e24476fc7ed5"
    }
}
```

