**Example 1: 修改主机备注信息**

修改主机备注信息

Input: 

```
tccli cwp ModifyMachineRemark --cli-unfold-argument  \
    --Remark remark for host1 \
    --Quuid 6cf3c132-aaa-bbbb-b08d-98be9421372a
```

Output: 
```
{
    "Response": {
        "RequestId": "8564b09e-0e04-4516-bb59-db09742503c2"
    }
}
```

