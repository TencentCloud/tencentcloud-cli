**Example 1: 批量修改责任人**

批量修改责任人

Input: 

```
tccli wedata UpdateBatchTaskInCharge --cli-unfold-argument  \
    --TaskIds 20230329162715992 \
    --InCharge ;peanutzhu; \
    --InChargeId ;100028578753;
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "TotalNumber": 1,
        "SuccessNumber": 1,
        "FailNumber": 0
    }
}
```

