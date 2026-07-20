**Example 1: 修改RemoteWrite 任务详情**

修改RemoteWrite 任务详情

Input: 

```
tccli cls ModifyRemoteWriteTask --cli-unfold-argument  \
    --TaskId xxx-xxx-xxx-xxx \
    --TopicId xxx-xxx-xxx-xxx \
    --Enable 0 \
    --Name test \
    --NetType 1 \
    --VpcId cls-xxxx \
    --Target Prometheus \
    --RemoteWriteURL http://127.0.0.1:80/api/v1/write \
    --AuthType 1 \
    --AuthInfo.Username test \
    --AuthInfo.Password passwrod \
    --AuthInfo.Token 
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx-xxx"
    }
}
```

