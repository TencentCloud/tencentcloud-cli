**Example 1: 查询规则表状态**



Input: 

```
tccli cfw DescribeTableStatus --cli-unfold-argument  \
    --Status 1 \
    --Direction 0 \
    --EdgeId edge-ppt3pi01 \
    --Area ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

