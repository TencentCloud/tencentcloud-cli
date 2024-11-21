**Example 1: 修改主机备注信息**

修改主机备注信息

Input: 

```
tccli cwp ModifyMachineRemark --cli-unfold-argument  \
    --Remark remark for host1 \
    --Quuid 5a540076-d38a-4078-aa98-e7c86371d322
```

Output: 
```
{
    "Response": {
        "RequestId": "8564b09e-0e04-4516-bb59-db09742503c2"
    }
}
```

