**Example 1: 创建按量计费的资源组纳管节点**



Input: 

```
tccli tione CreateBillingPostpaidSWInstances --cli-unfold-argument  \
    --ResourceGroupId xxx
```

Output: 
```
{
    "Response": {
        "FailedCVMInstances": [
            {
                "CVMInstanceId": "ins-zxc125",
                "FailedErrorMessage": "节点状态异常"
            }
        ],
        "RequestId": "d5405c55-a79d-4ecf-8b53-196859e45aa9"
    }
}
```

