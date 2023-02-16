**Example 1: DescribeWxCloudBaseRunSubNets**

查询子网

Input: 

```
tccli tcb DescribeWxCloudBaseRunSubNets --cli-unfold-argument  \
    --VpcId xx
```

Output: 
```
{
    "Response": {
        "SubNetIds": [
            "aa",
            "bb"
        ],
        "RequestId": "xx"
    }
}
```

