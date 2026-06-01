**Example 1: 行过滤修改**



Input: 

```
tccli tchousex OperateRowFilter --cli-unfold-argument  \
    --ApiType Create \
    --InstanceId instance-dgl3qg4g \
    --PolicyName 行过滤测试1 \
    --User user \
    --Database inside_db \
    --Tables ex_tmcam \
    --FilterExpr 'a > b'
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "ReturnData": "null",
        "RequestId": "fbc1b73b-9f1b-4726-891f-0f4b53cea636"
    }
}
```

