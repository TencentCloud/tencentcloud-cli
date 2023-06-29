**Example 1: 上报数据到cem**

适用于在cem已有实体，然后通过该接口上报数据。
流程： 沟通需求 -> cem建立实体 -> 配置字段映射 -> 提供业务唯一码，上报数据 

Data参数是一个序列化的数组

Input: 

```
tccli cem UploadData --cli-unfold-argument  \
    --Business xxxx \
    --Data [{"LicenseId":"1673424067","UserFullName":"测试","ProductSpec":"basic","NodeCount":200,"StartTime":1673424067,"Duration":5184000,"EndTime":1673424067,"DeployEnv":"容器部署","Status":2,"IsGenerate":1,"GranteeName":"test"}]
```

Output: 
```
{
    "Response": {
        "Response": [
            2680693150681112
        ],
        "RequestId": "abc"
    }
}
```

