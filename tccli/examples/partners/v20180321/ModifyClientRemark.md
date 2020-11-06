**Example 1: 修改客户备注名称为xxx**

代理商对其名下某代客，修改备注名称为xxx

Input: 

```
tccli partners ModifyClientRemark --cli-unfold-argument  \
    --ClientUin 123456789 \
    --ClientRemark xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

