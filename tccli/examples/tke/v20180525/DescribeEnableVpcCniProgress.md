**Example 1: 查看开启vpc-cni的任务进度，查询到任务失败**

用户调用EnableVpcCniNetworkType给GR集群附加vpc-cni网络能力，会创建一个异步任务。本接口用于查询该异步任务的进度，查询到任务进度失败。

Input: 

```
tccli tke DescribeEnableVpcCniProgress --cli-unfold-argument  \
    --ClusterId cls-abcdefgh
```

Output: 
```
{
    "Response": {
        "Status": "Failed",
        "ErrorMessage": "ipamd has not been installed yet",
        "RequestId": "defc0237-d413-4079-9faa-7f3ff928d224"
    }
}
```

