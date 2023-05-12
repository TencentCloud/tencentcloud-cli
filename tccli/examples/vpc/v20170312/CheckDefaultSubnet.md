**Example 1: 预判是否可建默认子网**

预判是否可建默认子网

Input: 

```
tccli vpc CheckDefaultSubnet --cli-unfold-argument  \
    --Zone ap-guangzhou-1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Result": true
    }
}
```

