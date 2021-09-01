**Example 1: 返回成功**



Input: 

```
tccli ba SyncIcpOrderWebInfo --cli-unfold-argument  \
    --IcpOrderId 30159962067561775 \
    --SourceWebId 1000230 \
    --TargetWebIds 10023 10024 \
    --SyncFields urlQCloud siteLiveBodyVerifyUrl
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx-xxx"
    }
}
```

