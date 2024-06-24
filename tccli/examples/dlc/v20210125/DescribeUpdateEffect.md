**Example 1: 获取引擎变配影响范围**



Input: 

```
tccli dlc DescribeUpdateEffect --cli-unfold-argument  \
    --DataEngineName abc \
    --Size 64 \
    --MinClusters 1
```

Output: 
```
{
    "Response": {
        "NeedRestart": false,
        "RequestId": "41c4cb8e-23ef-43b2-aed0-6103a0b21bb6"
    }
}
```

