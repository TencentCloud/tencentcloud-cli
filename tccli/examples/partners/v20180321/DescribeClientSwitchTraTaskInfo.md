**Example 1: 查询客户的交易类型切换任务信息**



Input: 

```
tccli partners DescribeClientSwitchTraTaskInfo --cli-unfold-argument  \
    --ClientUin 100000000001 \
    --SwitchType 2
```

Output: 
```
{
    "Response": {
        "ClientUin": "100000000001",
        "RequestId": "cdfe0563-f4c5-4a2c-9420-0f92dc360e66",
        "Result": "ok",
        "ResultMsg": "",
        "SwitchType": "代采",
        "SwitchUrl": "https://partner.cloud.tencent.com/translate?taskId=xxxxxxxxxxxxxxxxxxx"
    }
}
```

