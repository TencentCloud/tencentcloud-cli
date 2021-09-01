**Example 1: 会员间交易-不验证**



Input: 

```
tccli cpdp QueryMemberTransaction --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --FunctionFlag 9 \
    --OutSubAcctNo ' 1234000000021018' \
    --OutMemberCode ' YAPI100015' \
    --OutSubAcctName demo \
    --InSubAcctNo ' 1234000000021028' \
    --InMemberCode ' YAPI100016' \
    --InSubAcctName demo \
    --TranAmt 10 \
    --TranFee 0 \
    --TranType 01 \
    --Ccy RMB \
    --OrderNo O2019120667
```

Output: 
```
{
    "Response": {
        "RequestId": "5db16324-2c31-4848-adde-d45ea658fbbb"
    }
}
```

