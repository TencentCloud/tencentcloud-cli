**Example 1: 预判是否可建默认子网**



Input: 

```
tccli vpc CheckDefaultSubnet --cli-unfold-argument  \
    --Zone ap-guangzhou-1
```

Output: 
```
{
    "Response": {
        "Result": true
    }
}
```

