**Example 1: 修改数据转发**



Input: 

```
tccli iotvideo ModifyDataForward --cli-unfold-argument  \
    --ProductId TOIDHQ3AOQ, \
    --ForwardAddr [{"forward":{"api":"http://127.0.0.1:1080/sub.php"}}] \
    --DataChose 1
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e07e"
    }
}
```

