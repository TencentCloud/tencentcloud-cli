**Example 1: 批量修改资源组**

批量修改资源组

Input: 

```
tccli wedata UpdateBatchTaskResourceGroup --cli-unfold-argument  \
    --TaskIds 20230425232039882 20230425232037110 \
    --ResourceGroup 20230425232039882 \
    --EtlResourceGroup 20230425232037110
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "TotalNumber": 1,
        "SuccessNumber": 0,
        "FailNumber": 1
    }
}
```

